let currentCalc = "";
let num_btn0 = document.querySelector("#num0");
let num_btn1 = document.querySelector("#num1");
let num_btn2 = document.querySelector("#num2");
let num_btn3 = document.querySelector("#num3");
let num_btn4 = document.querySelector("#num4");
let num_btn5 = document.querySelector("#num5");
let num_btn6 = document.querySelector("#num6");
let num_btn7 = document.querySelector("#num7");
let num_btn8 = document.querySelector("#num8");
let num_btn9 = document.querySelector("#num9");
let plus_btn = document.querySelector("#plus");
let minus_btn = document.querySelector("#minus");
let multiply_btn = document.querySelector("#multiply");
let divide_btn = document.querySelector("#divide");
let equals_btn = document.querySelector("#equals");
let clear_btn = document.querySelector("#clear");


num_btn0.addEventListener("click",
function (e)
{
currentCalc = currentCalc + e.target.textContent;
let disp = document.querySelector("#display");
disp.textContent = currentCalc;
});

num_btn1.addEventListener("click",
function (e)
{
currentCalc = currentCalc + e.target.textContent;
let disp = document.querySelector("#display");
disp.textContent = currentCalc;
});

num_btn2.addEventListener("click",
function (e)
{
currentCalc = currentCalc + e.target.textContent;
let disp = document.querySelector("#display");
disp.textContent = currentCalc;
});

num_btn3.addEventListener("click",
function (e)
{
currentCalc = currentCalc + e.target.textContent;
let disp = document.querySelector("#display");
disp.textContent = currentCalc;
});

num_btn4.addEventListener("click",
function (e)
{
currentCalc = currentCalc + e.target.textContent;
let disp = document.querySelector("#display");
disp.textContent = currentCalc;
});

num_btn5.addEventListener("click",
function (e)
{
currentCalc = currentCalc + e.target.textContent;
let disp = document.querySelector("#display");
disp.textContent = currentCalc;
});

num_btn6.addEventListener("click",
function (e)
{
currentCalc = currentCalc + e.target.textContent;
let disp = document.querySelector("#display");
disp.textContent = currentCalc;
});

num_btn7.addEventListener("click",
function (e)
{
currentCalc = currentCalc + e.target.textContent;
let disp = document.querySelector("#display");
disp.textContent = currentCalc;
});

num_btn8.addEventListener("click",
function (e)
{
currentCalc = currentCalc + e.target.textContent;
let disp = document.querySelector("#display");
disp.textContent = currentCalc;
});

num_btn9.addEventListener("click",
function (e)
{
currentCalc = currentCalc + e.target.textContent;
let disp = document.querySelector("#display");
disp.textContent = currentCalc;
});

plus_btn.addEventListener("click",
function (e)
{
currentCalc = currentCalc + e.target.textContent;
let disp = document.querySelector("#display");
disp.textContent = currentCalc;
});

minus_btn.addEventListener("click",
function (e)
{
currentCalc = currentCalc + e.target.textContent;
let disp = document.querySelector("#display");
disp.textContent = currentCalc;
});

multiply_btn.addEventListener("click",
function (e)
{
currentCalc = currentCalc + e.target.textContent;
let disp = document.querySelector("#display");
disp.textContent = currentCalc;
});

divide_btn.addEventListener("click",
function (e)
{
currentCalc = currentCalc + e.target.textContent;
let disp = document.querySelector("#display");
disp.textContent = currentCalc;
});

equals_btn.addEventListener("click",
function (e)
{
let disp = document.querySelector("#display");
disp.textContent = eval(currentCalc);
currentCalc = "";
});

clear_btn.addEventListener("click",
function (e)
{
currentCalc = currentCalc + e.target.textContent;
let disp = document.querySelector("#display");
disp.textContent = currentCalc = "";
});