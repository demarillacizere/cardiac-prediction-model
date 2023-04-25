# cardiac-prediction-model
<h1>This is a Machine Learning Model that predicts Heart Diseases with the help of Framingham Data Set</h1>

<h3>Framingham dataset:</h3>

<b>We got thr dataset from Kaggle, and it is from an ongoing ongoing cardiovascular study on residents of the town of Framingham. The classification goal is to predict whether the patient has 10-year risk of future coronary heart disease.The dataset provides the patients’ information. It includes over 4,240 records and 15 attributes.</b>
<br></br>
<hr></hr>
<h3>Attributes:</h3>
<hr></hr>
<ol><b>
    <li>sex: male(1) or female(0);(Nominal)</li > 
    <li>age: age of the patient;(The age is continuous )</li >
    <li>currentSmoker: whether or not the patient is a current smoker (Nominal)</li >
    <li>cigsPerDay: the number of cigarettes that the person smoked on average in one day.(can be considered continuous as one can have any number of cigarretts, even half a           cigarette.)</li >
    <li>BPMeds: whether or not the patient was on blood pressure medication (Nominal)</li >
      <li>prevalentStroke: whether or not the patient had previously had a stroke (Nominal)</li >
      <li>prevalentHyp: whether or not the patient was hypertensive (Nominal)</li >
      <li>diabetes: whether or not the patient had diabetes (Nominal)</li >
      <li>totChol: total cholesterol level (Continuous)</li >
      <li>sysBP: systolic blood pressure (Continuous)</li >
      <li>diaBP: diastolic blood pressure (Continuous)</li >
      <li>BMI: Body Mass Index (Continuous)</li >
      <li>heartRate: heart rate (Continuous - In medical research, variables such as heart rate though in fact discrete, yet are considered continuous because of large number             of possible values.)</li >
      <li>glucose: glucose level (Continuous)</li >
      <li>10 year risk of coronary heart disease CHD (binary: “1”, means “Yes”, “0” means “No”) - Target Variable</li >
    </b>
  </ol>

<hr></hr>
<h2>Objective: Build a classification model that predicts heart disease.</h2>(note the target column to predict is 'TenYearCHD' where CHD = Coronary heart disease) 

<h1>Hosting a Node.js application on Heroku</h1>
      <li>First, make sure you have Node.js and NPM installed on your local machine.</li >
      <li>Create a new directory for your application and navigate to it using the command line.</li >
      <li>Initialize a new Node.js project by running the command npm init and following the prompts.</li >
      <li>Install the required dependencies for your application using the command npm install.</li >
      <li>Clone this repository to your folder</li >
      <li>Create a new Heroku app by running the command heroku create.</li >
      <li>Push your code to the Heroku app using the command git push heroku master.</li >
      <li>Open your application in the browser by running the command heroku open.</li >
