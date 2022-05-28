const food = []
const items = document.getElementById('items')
const butn = document.getElementById('butn')
const lenfood = 27 // no.of food items

// creating a list of all food item elements in the html file
for (let i=0;i<lenfood;i++){
    let k = "food"+ (i+1).toString();
    const r = document.getElementById(k)
    food.push(r);
}

//adding event listener to each input(checkbox)
for (let i=0;i<lenfood;i++){
    food[i].addEventListener('change',e => {
        if(e.target.checked){
             const item = document.createElement("li")
             item.innerHTML = food[i].value;
             items.appendChild(item)
        }
        else{
            items.innerHTML=''
            for(let i=0; i<lenfood ;i++){
                    food[i].checked = false;
            }
        }
    })
}
