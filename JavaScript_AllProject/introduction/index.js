//Activity 1
// alert("Hello")
// var num=5
// var st="ghamdan"
// var bo= true
// var flo= 2.3
// alert(typeof(num))
// alert(typeof(st))
// alert(typeof(bo))
// alert(typeof(flo))
// console.log(1)
// var x= prompt("enter name :")
// console.log("hi "+x)
// alert(x.length)
//-----End 1 ------

//Activity 2 - Part 1 for week
//This function calculate weekss Since Birthdate
// function calculateWeeksSinceBirthdate() {
//   var birthdate = prompt("Please enter your birthdate (YYYY-MM-DD):");
  
//   var birthdateObj = new Date(birthdate);
//   var currentDate = new Date();
//   var timeDiff = Math.abs(currentDate.getTime() - birthdateObj.getTime());
//   var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));
  
//   var weeks;
  
//   if (diffDays < 7) {
//     weeks = 0;
//   } else {
//     weeks = Math.floor(diffDays / 7);
//   }
  
//   return weeks;
// }

// var weeksSinceBirth = calculateWeeksSinceBirthdate();

// console.log("Number of weeks since birth: " + weeksSinceBirth);



// Part 2 for Days
// This function calculate Days Since Birthdate
function calculateDaysSinceBirthdate() {
  var birthdate = prompt("Please enter your birthdate (YYYY-MM-DD):");
  
  var birthdateObj = new Date(birthdate);
  var currentDate = new Date();
  var timeDiff = Math.abs(currentDate.getTime() - birthdateObj.getTime());
  var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));
  
  return diffDays;
}

var daysSinceBirth = calculateDaysSinceBirthdate();

console.log("Number of days since birth: " + daysSinceBirth);
//-----End 2 ------


//Activity 3 - calculateBMI
// function calculateBMI(weight, height) {
//     var bmi = weight / (height * height);
//     return bmi;
//   }
  
//   function classifyBMI(bmi) {
//     if (bmi < 17) {
//       return "Underweight";
//     } else if (bmi >= 17 && bmi < 25) {
//       return "Normal weight";
//     } else if (bmi >= 25 && bmi < 30) {
//       return "Overweight (Fat)";
//     } else if (bmi >= 30 && bmi < 35) {
//       return "Obese Class I";
//     } else if (bmi >= 35 && bmi < 40) {
//       return "Obese Class II (Severely obese)";
//     } else if (bmi >= 40) {
//       return "Obese Class III (Very severely obese)";
//     }
//   }
  
//   // Example usage
//   var weight = 70; // weight in kilograms
//   var height = 1.75; // height in meters
//   var bmi = calculateBMI(weight, height);
//   var classification = classifyBMI(bmi);
//   console.log("BMI: " + bmi);
//   console.log("Classification: " + classification);
//-----End 3 ------




//Activity 4 - fibonacci list
// function fibonacciSeries(n) {
//   var fibSeries = [0, 1]; 
  
//   if (n <= 2) {
//     return fibSeries.slice(0, n); 
//   }
  
//   for (var i = 2; i < n; i++) {
//     var nextNum = fibSeries[i - 1] + fibSeries[i - 2]; 
//     fibSeries.push(nextNum); 
//   }
  
//   return fibSeries;
// }

// var n = prompt("Enter the number you want : "); 
// var fibonacci = fibonacciSeries(n);
// console.log(fibonacci);
//-----End 4 ------
