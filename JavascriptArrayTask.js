function removeInvalidPriorityNumbers(array){
const validArray = [];
for(let index = 0; index < array.length; index += 1){
if(array[index] != 0 && array[index] != 6){
validArray.push(array[index]);
}

}
return validArray;
}


function getHighScoringCustomers(customers){
const newObject = customers.filter(customersData => customersData.score >= 80 && customersData.score <= 100);
newObject.sort((a,b) => b.score - a.score);
return newObject;
}









const array = [0,0,1,0,6,6,0,0,5,2,6,3,4,0];
console.log("1.",removeInvalidPriorityNumbers(array));

const scores = [{name: "Emmanw",score: 89},{name: "Emmanuel",score: 92},{name: "Emma",score: 10},{name: "Emman",score: 91},{name: "name",score: 100}];
console.log("2.", getHighScoringCustomers(scores));
