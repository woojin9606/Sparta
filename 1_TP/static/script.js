// let cli = document.getElementById("click");
let dis = document.getElementById("display");
let dis2 = document.getElementById("display2");

function Display() {
    if (dis.style.display == 'none'){
        dis.style.display = 'flex';
    } else {
        dis.style.display='none';
    }
    if (dis2.style.display == 'none'){
        dis2.style.display = 'flex';
    } else {
        dis2.style.display='none';
    }
}

function hide(timestamp) {
    // const hide_id = timestamp + "_parent";
    const hide_div = document.getElementById(timestamp+"_parent");
    hide_div.style.display = 'none'
}