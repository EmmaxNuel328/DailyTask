function removeInvalidPriorityNumbers(array){
const validArray = [];
for(let index = 0; index < array.length; index += 1){
if(array[index] != 0 && array[index] != 6){
validArray.push(array[index]);
}


}
return validArray;
}


const array = [0,0,1,0,6,6,0,0,5,2,6,3,4,0];
console.log("1.",removeInvalidPriorityNumbers(array));

