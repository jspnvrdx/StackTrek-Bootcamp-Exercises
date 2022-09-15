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
        const tag = document.createElement("input");
        tag.setAttribute("type", "checkbox");
        tag.setAttribute("name", id.slice(0,-1));
        tag.setAttribute("id", x.split(" ")[0]);
        const label = document.createElement("label");
        label.setAttribute("for", x.split(" ")[0])
        const text = document.createTextNode(x);
        label.appendChild(text);
        tag.appendChild(label);
        idtag.appendChild(tag)
        
        const br = document.createElement("br");
        idtag.appendChild(br);
    }
}

getList(meats, meatId);
getList(soapsAndShampoos, soapId);
getList(vegetables, vegetableId);
getList(cannedGoods, cannedGoodsId);