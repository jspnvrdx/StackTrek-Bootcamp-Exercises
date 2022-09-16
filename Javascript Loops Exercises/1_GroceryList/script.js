const meats = ["Fish","Chicken","Pork","Beef"];
const soapsAndShampoos = ["Head n Shoulders","safeguard","dove","rejoice"];
const vegetables = ["Carrots","Pechay","Talong","Sitaw"];
const cannedGoods = ["Corned Beef","sardines","spam","beef loaf"];

const meatId = "meats";
const soapId = "soaps";
const vegetableId = "vegetables";
const cannedGoodsId = "canned-goods";

function getList(list, id) {
    const idtag = document.getElementById(id);
    for (let x of list){
        // create a label
        var label = document.createElement("label");
        // create a checkbox
        var checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.name = id.slice(0,-1);
        checkbox.id = x.split(" ")[0];
        
        label.setAttribute("for", x.split(" ")[0]);
        var text = document.createTextNode(x);

        label.appendChild(checkbox);
        label.appendChild(text);
        // checkbox.appendChild(label);
        idtag.appendChild(label);
        
        var br = document.createElement("br");
        idtag.appendChild(br);
    }
}

getList(meats, meatId);
getList(soapsAndShampoos, soapId);
getList(vegetables, vegetableId);
getList(cannedGoods, cannedGoodsId);