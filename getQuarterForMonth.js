function getQuarterForMonth(monthNumber){
//let NameOfMonth = monthName.toLowerCase();
if(monthNumber > 0 && monthNumber <= 3){
return "month","is part of the first quarter";
} 
if(monthNumber > 3 && monthNumber <= 6){
return "month","is part of the second quarter";
} 
if(monthNumber > 6 && monthNumber <= 9){
return "month","is part of the third quarter";
} 
if(monthNumber > 9 && monthNumber <= 12){
return "month","is part of the fourth quarter";
} 
if(monthNumber <= 0 || monthNumber > 12){
return "INVALID INPUT";
} 
}



//const userInput = prompt("Enter Month Number:");
let userInput = 11;
console.log("Month",userInput,getQuarterForMonth(userInput));




