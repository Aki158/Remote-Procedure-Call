import json
import math
import os
import socket


def main():
    funcHashmap = {
        'floor' : floor,
        'nroot' : nroot,
        'reverse' : reverse,
        'validAnagram' : validAnagram,
        'sort' : sort
    }

    paramCheckHashmap = {
        'floor' : 'double',
        'nroot' : '[int,int]',
        'reverse' : 'string',
        'validAnagram' : '[string,string]',
        'sort' : 'string[]'
    }

    # ソケットを作成する
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # アドレスを定義する
    serverAddress = '127.0.0.1'

    try:
        # 前回の実行でソケットファイルが残っていた場合、そのファイルを削除する
        os.unlink(serverAddress)
    except FileNotFoundError:
        pass

    # サーバのアドレスをソケットに紐付ける
    sock.bind(serverAddress)

    # ソケットが接続要求を待機する
    sock.listen(1)
    
    # クライアントからの接続を受け入れる
    connection, _ = sock.accept()

    try:
        while True:
            print('--------------------')
            # クライアントのソケットからのデータ(json形式)を受信する
            data = connection.recv(1024)

            # 受け取ったデータはバイナリ形式なので、それを文字列に変換する
            dataStr =  data.decode('utf-8')

            # 受信したデータを表示する
            print('received data : {}'.format(dataStr))

            receivedData = json.loads(data)
            method = receivedData['method']
            params = receivedData['params']
            paramTypes = receivedData['param_types']
            id = receivedData['id']

            # JSON形式のデータ(結果、結果の型、同じリクエストID)をクライアントに送り返す
            if method in funcHashmap:
                # パラメータの検証を行う
                if paramCheckHashmap[method] != str(paramTypes):
                    sendData = 'Invalid parameter'
                else:
                    results = funcHashmap[method](params)
                    resultsType = resultTypeCondition(results)
                    sendHashmap = {
                        'results' : str(results),
                        'result_type' : resultsType,
                        'id' : id
                    }
                    sendData = json.dumps(sendHashmap)
            else:
                sendData = 'Function not found'

            connection.sendall(sendData.encode('utf-8'))
            print('sent data : {}'.format(sendData))
    finally:
        # 最後にソケットを閉じてリソースを解放する
        print('closing socket')
        sock.close()

# typeを調べる
def resultTypeCondition(t):
    if isinstance(t, bool):
        return 'bool'
    elif isinstance(t, int):
        return 'int'
    elif isinstance(t, float):
        return 'double'
    elif isinstance(t, str):
        return 'str'
    elif isinstance(t, list):
        return 'list'
    else:
        return "It was a type I wasn't expecting" 

# 10進数xを最も近い整数に切り捨て、その結果を整数で返す
def floor(x):
    return int(math.floor(x))

# 方程式r^n=xにおける、rの値を計算する
def nroot(arr):
    return math.pow(arr[1],1/arr[0])

# 入力文字列の逆である新しい文字列を返す
def reverse(s):
    return s[::-1]

# 2つの入力文字列が互いにアナグラムであるかどうかを示すブール値を返す
# ここでは大文字と小文字の区別はつけずスペースは文字として扱わないものとする
def validAnagram(strArr):
    s1 = strArr[0].replace(' ', '').lower()
    s2 = strArr[1].replace(' ', '').lower()
    hashmap1 = {}
    hashmap2 = {}

    if len(s1) != len(s2):
        return False
    
    for i in s1:
        if i not in hashmap1:
            hashmap1[i] = 1
        else:
            hashmap1[i] += 1

    for i in s2:
        if i not in hashmap2:
            hashmap2[i] = 1
        else:
            hashmap2[i] += 1
    
    return hashmap1 == hashmap2

# 入力である文字列の配列をソートして、ソート後の文字列rの配列を返す
def sort(strArr):
    return sorted(strArr)


if __name__ == '__main__':
    main()
