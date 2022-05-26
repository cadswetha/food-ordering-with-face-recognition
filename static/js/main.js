const food = []
const items = document.getElementById('items')
const lenfood = 27
for (let i=0;i<lenfood;i++){
    let k = "food"+ (i+1).toString();
    const r = document.getElementById(k)
    food.push(r);
}
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

