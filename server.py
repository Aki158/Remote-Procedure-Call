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
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    # アドレスを定義する
    #server_address = '/udp_socket_file'
    server_address = '127.0.0.1'

    try:
        # 前回の実行でソケットファイルが残っていた場合、そのファイルを削除する
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    while True:
        # サーバのアドレスをソケットに紐付ける
        sock.bind(server_address)

        print('\nwaiting to receive message')

        # クライエントのソケットからのデータ(json形式)を受信する
        data, address = sock.recvfrom(4096)

        # 受信したデータを表示する
        print('received data : {}'.format(data))

        receivedData = json.loads(data)
        method = receivedData['method']
        params = receivedData['params']
        paramTypes = receivedData['param_types']
        id = receivedData['id']

        # JSON形式のデータ(結果、結果の型、同じリクエストID)をクライエントに送り返す
        if method in funcHashmap:
            # パラメータの検証を行う
            if paramCheckHashmap[method] != str(paramTypes):
                sendData = 'Invalid parameter\n \
                    Input parameter : \
                    double or [int,int] or string or [string,string] or string[]'
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

        sent = sock.sendto(sendData, address)
        print('sent data : {}'.format(sendData))

        quitQuestion = input('Do you want to quit?(Y/N)').lower()
        if quitQuestion == 'y':
            break
    
    # 最後にソケットを閉じてリソースを解放する
    print('closing socket')
    sock.close()

# typeを調べる
def resultTypeCondition(t):
    if isinstance(t, int):
        return 'int'
    elif isinstance(t, float):
        return 'double'
    elif isinstance(t, str):
        return 'str'
    elif isinstance(t, bool):
        return 'bool'
    elif isinstance(t, list):
        return 'list'
    else:
        return "It was a type I wasn't expecting"  

# 10進数xを最も近い整数に切り捨て、その結果を整数で返す
def floor(x):
    return int(math.floor(x))

# 方程式r^n=xにおける、rの値を計算する
def nroot(n, x):
    return math.pow(x,1/n)

# 入力文字列の逆である新しい文字列を返す
def reverse(s):
    return s[::-1]

# 2つの入力文字列が互いにアナグラムであるかどうかを示すブール値を返す
# ここでは大文字と小文字の区別はつけずスペースは文字として扱わないものとする
def validAnagram(str1, str2):
    s1 = str1.replace(' ', '').lower()
    s2 = str2.replace(' ', '').lower()
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