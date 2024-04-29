
const url = window.location.href;
const quizBox = document.getElementById('quiz-box');
const qcloseBox = document.getElementById('close-box');

const scoreBox = document.getElementById('scrore-box');
const resaultBox = document.getElementById('resault-box');
const TimerBox = document.getElementById('timer-box');
const closeBox = document.getElementById('close-box');


const startsTimer = (vaqti) => {
  console.log(vaqti)
  let minutes = vaqti - 1;
  let seconds = 60;
  let timer = setInterval(() => {
    seconds--;
    if (seconds < 0) {
      seconds = 59;
      minutes--;
    }
    TimerBox.innerHTML = `<br>${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}</br>`;
    if (minutes === 0 && seconds === 0) {
      TimerBox.innerHTML = `00:00`;
      let clearVaqt = setTimeout(() => {
        clearInterval(timer);
        clearTimeout(clearVaqt);
        alert('vaqt tugadi');
        sendData();
      }, 500);
    }
  }, 1000);
};


$.ajax({
  type: 'GET',
  url: `${url}data`,
  success: (response) => {
    const data = response.data;
    console.log(response.vaqti)
    data.forEach((element) => {
      for (const [questions, answers] of Object.entries(element)) {
        quizBox.innerHTML += `
          <hr>
          <div class="mt-2 border p-8 rounded-lg shadow-md shadow-black w-full">
            <b>${questions}</b>
          </div>
        `;
        answers.forEach((answer) => {
          quizBox.innerHTML += `
            <div class="flex justify-start items-center gap-3 p-5">
              <input type="radio" class="ans" id="${questions}-${answer}" name="${questions}" value="${answer}">
              <label for="${questions}">${answer}</label>
            </div>
          `;
        });
      }
    });
    startsTimer(response.vaqti);
  },
  error: (error) => {
    console.log(error);
  }
});



const quizForm = document.getElementById("quiz-form");
const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

const sendData = () => {
  const elements = [...document.getElementsByClassName("ans")];
  const data = {};
  data['csrfmiddlewaretoken'] = csrfToken;
  elements.forEach((el) => {
    if (el.checked) {
      data[el.name] = el.value;
    } else {
      if (!data[el.name]) {
        data[el.name] = null;
      }
    }
  });
 

  $.ajax({
    type: `POST`,
    url: `${url}save/`,
    data: data,
    success: function(response){
        const resolt=response.results
        quizForm.classList.add('hidden')
        closeBox.classList.add('hidden')
        scoreBox.innerHTML=`${response.passed ? 'Congratulations ': 'Sizning Natijanggiz'} ${response.score.toFixed(2)}%`
        resolt.forEach(res=>{
            const resDev= document.createElement("div")
            for (const [question, resp] of Object.entries(res)){
                resDev.innerHTML+=question
                const cls=['p-3', 'text-center', 'text-sm',"w-96", "rounded-lg", "m-6", 'text-sm', 'text-rose-50' ]
                resDev.classList.add(...cls)
                if (resp=="javob berilmagan"){
                    resDev.innerHTML+="Javob berilmadi"
                    resDev.classList.add('bg-red-300')
                }else{
                    const answers=resp['nateja_a']
                    const natejs=resp['nateja']
                    if (answers==natejs){
                        resDev.classList.add("bg-blue-600")
                        resDev.innerHTML+=` To'g'ri Javob Berdinggiz  ${answers}`
                    }else{
                        resDev.classList.add("bg-red-700")
                        resDev.innerHTML +=`To'g'ri javob: ${natejs}`
                        resDev.innerHTML+=` Sizning javob: ${answers}`
                    }
                }
            }
            resaultBox.append(resDev)

        })
    },
    error: function(error){
        console.log(error)
    }
   })
}
function stopTextColor() {
  clearInterval(timer);
  clearTimeout(clearVaqt);

  clearVaqt=null;
  // release our intervalID from the variable
  timer = null;
}


quizForm.addEventListener('submit', e=>{
    e.preventDefault();
    // clearTimeout(clearVaqt);
    stopTextColor;
    // e.clearInterval(timer);
    sendData();
});
