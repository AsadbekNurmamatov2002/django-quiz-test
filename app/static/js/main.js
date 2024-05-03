
const modelBtns=[...document.getElementsByClassName("model-btn")]
const modelBody=document.getElementById('model-body')
const stopBtn=document.getElementById('btn-stop')
const startBtn=document.getElementById('btn-start')

modelBtns.forEach(modelBtn=> modelBtn.addEventListener('click', ()=>{
    const pk=modelBtn.getAttribute("data-pk")
    const dataname=modelBtn.getAttribute("data-name")
    const databody=modelBtn.getAttribute("data-body")
    const datasoni=modelBtn.getAttribute("data-soni")
    const datafoiz=modelBtn.getAttribute("data-foiz")
    const datatime=modelBtn.getAttribute("data-vaqt")
   console.log("pk",pk)
    modelBody.innerHTML+=`
    <h3 class="font-bold text-lg">${dataname} !</h3>
    <p class="py-4"> ${databody}</p>
    <h4>${datasoni}</h4> vaqti: <h4>${datatime}</h4>
    <p>${datafoiz}</p>
    `
    startBtn.addEventListener('click',()=>{
        window.location.href = window.location.href + pk
    })
}))



// data  json


