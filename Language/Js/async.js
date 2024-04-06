/*
Conclusion:
1. console.log will be printed firstly
2. within the function, the code will be executed by order
*/

async function delayedExecutionOne() {
    console.log('Execution1 started');
    await new Promise(resolve => setTimeout(resolve, 5000));
    console.log('Execution1 completed');
}
  

async function delayedExecutionTwo() {
    console.log('Execution2 started');
    await new Promise(resolve => setTimeout(resolve, 3000));
    console.log('Execution2 completed');
}

delayedExecutionOne();
delayedExecutionTwo();
console.log("Whether the console.log is firstly executed or not?")