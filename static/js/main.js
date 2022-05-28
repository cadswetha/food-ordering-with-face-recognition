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

//event listener for the button
butn.addEventListener('click',() => {
    // getting user mailid using jinja template in html file
    let mailid = document.getElementById('my-data').innerHTML;

    //getting all the child elements of <ul></ul>
    let children = items.children;

    //a string that stores all the selected food items
    let foodlist = ""
    for (let i=0;i<children.length;i++){
        let child = children[i];
        foodlist+= child.innerHTML+"\n";
    }

    // console.log(mailid);

    items.innerHTML="orders saved!"
    // unchecking all the selected items after saving
    for(let i=0; i<lenfood ;i++){
        food[i].checked = false;
    }

    // //once the save button is clicked , generating a query 
    // var data = new URLSearchParams();
    // data.append("email", mailid);
    // data.append("content", foodlist);

    // // ****change the url afterwards
    // var url = " http://127.0.0.1:5500/register_submit" + data.toString();
    // location.href = url;
})

