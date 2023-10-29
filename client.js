const net = require('node:net');
const serverAddress = '127.0.0.1'

class Client{
    constructor(address){
        this.sock = net.createConnection(address);
        this.sock.setTimeout(30000);
        this.sock.on('data', (data) => {
            console.log(data.toString());
        });
        this.sock.on('end', () => {
            console.log('disconnected from server');
        });
        this.sock.on('error', (err) => {
            console.log(err.message);
        });
    }

    write(data){
        this.sock.write(data);
    }
}

messageList = [
    {
        "method": "floor",
        "params": 5.345,
        "param_types": "double",
        "id": 0
    },
    {
        "method": "nroot",
        "params": [3,8],
        "param_types": "[int,int]",
        "id": 1
    },
    {
        "method": "reverse",
        "params": "hello",
        "param_types": "string",
        "id": 2
    },
    {
        "method": "validAnagram",
        "params": ["anagram","ano grew"],
        "param_types": "[string,string]",
        "id": 3
    },
    {
        "method": "sort",
        "params": ["Nice","to","meet","you"],
        "param_types": "string[]",
        "id": 4
    },
    {
        "method": "floor",
        "params": 5.345,
        "param_types": "float",
        "id": 5
    },
    {
        "method": "subtract",
        "params": [42,23],
        "param_types": "[int,int]",
        "id": 6
    }
]

let client = new Client(serverAddress);

async function getInput(){
    await sleep(1000);
    console.log('--------------------');
    readline.question('Please enter a number between 0 and 6 : ', (input) => {
        if(input === 'exit'){
            readline.close();
        }
        else{
            const message = messageList[parseInt(input, 10)];
            console.log(message);
            client.write(JSON.stringify(message));
            getInput();
        }
    })
}

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

async function sleep(ms) {
    return new Promise(r => setTimeout(r, ms));
}

getInput();

