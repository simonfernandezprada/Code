//Selection of the elements
const clear = document.querySelector(".clear");
const dateElement = document.getElementById("date");
const list = document.getElementById("list");
const input = document.getElementById("input");

//Classes names
const CHECK = "fa-check-circle";
const UNCHECK = "fa-circle-thin";
const LINE_THROUGH = "lineThrough";

//Variables
let LIST, id;

//Get item from localstorage
let data = localStorage.getItem("TODO");

//Check if data is not empty
if(data){
  LIST = JSON.parse(data);
  id = LIST.lenght;
  loadList(LIST);
}else{
  LIST = [];
  id = 0;
}

//Load items t the user's interface
function loadList(array){
  array.forEach(function(item){
    addToDo(item.name, item.id, item.done, item.trash);
  });
}

// Clear the local Storage
clear.addEventListener("click", function(){
  localStorage.clear();
  location.reload();
});

//Shows todays date
const options = {weekday:"long", month:"short", day:"numeric"};
const today  = new Date();

dateElement.innerHTML = today.toLocaleDateString("en-US", options);

//Add to do funtion
function addToDo(toDo, id, done, trash){

    if(trash){ return; }

    const DONE = done ? CHECK : UNCHECK;
    const LINE = done ? LINE_THROUGH : "";
    const item = `<li class="item">
                    <i class="fa ${DONE} co" job="complete" id="${id}"></i>
                    <p class="text ${LINE}">${toDo}</p>
                    <i class="fa fa-trash-o de" job="delete" id="${id}"></i>
                  </li>
                  `;
    const position = "beforeend";

    list.insertAdjacentHTML(position,item);
};

//Add an item when user hits enter
document.addEventListener("keyup",function(even){
    if(event.keyCode == 13){
      const toDo = input.value;

      // If the input isnt empty
      if(toDo) {
        addToDo(toDo, id, false, false);

        LIST.push({
          name : toDo,
          id : id,
          done : false,
          trash : false
        });

        //Add item to localstorage (must be added where LIST array is updated)
        localStorage.setItem("TODO", JSON.stringify(LIST));

        id++;
      }
      input.value = "";
    }
});

//What happens whenthe user presses complete
function completeToDo(element){
  element.classList.toggle(CHECK);
  element.classList.toggle(UNCHECK);
  element.parentNode.querySelector(".text").classList.toggle(LINE_THROUGH);

  LIST[element.id].done = LIST[element.id].done ? false : true;
}

//What happens when the user removes a todo
function removeToDo(element){
  element.parentNode.parentNode.removeChild(element.parentNode);

  LIST[element.id].trash = true;
}

list.addEventListener("click", function(event){
  const element = event.target;
  const elementJob = element.attributes.job.value;

  if(elementJob == "complete"){
    completeToDo(element);
  }else if(elementJob == "delete"){
    removeToDo(element);
  }
  //Add item to localstorage (must be added where LIST array is updated)
  localStorage.setItem("TODO", JSON.stringify(LIST));
});