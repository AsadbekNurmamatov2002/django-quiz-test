
const modelBtns=[...document.getElementsByClassName("model-btn")]
const modelBody=document.getElementById('model-body')
const stopBtn=document.getElementById('btn-stop')
const startBtn=document.getElementById('btn-start')

modelBtns.forEach(modelBtn=> modelBtn.addEventListener('click', ()=>{
    const pk=modelBtn.getAttribute("data-pk")
    const name=modelBtn.getAttribute("data-name")
    const body=modelBtn.getAttribute("data-body")
    const soni=modelBtn.getAttribute("data-soni")
    const foiz=modelBtn.getAttribute("data-foiz")
    const time=modelBtn.getAttribute("data-vaqt")

    modelBody.innerHTML=`
<dialog id="my_modal_3" class="modal">
  <div class="modal-box">
    <form method="dialog">
      <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>
    </form>
    <h3 class="font-bold text-lg">${name} !</h3>
    <p class="py-4"> ${body}</p>
    <h4>${soni}</h4> vaqti: <h4>${time}</h4>
    <p>${foiz}</p>
  </div>
</dialog>
    `
    startBtn.addEventListener('click',()=>{
        window.location.href = window.location.href + pk
    })
}))



// data  json


