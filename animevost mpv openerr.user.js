// ==UserScript==
// @name         animevost mpv openerr
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://reansn0w.github.io/AnimeVostORGCustomPlayer/New/*
// @icon         https://www.google.com/s2/favicons?domain=github.io
// @grant        none
// ==/UserScript==


window.onload = function() {
    var allCards = document.querySelectorAll("div.card").forEach((item, index)=>{
        var htmlInner = item.innerHTML
        var img = item.querySelector("img")
        var name = img.getAttribute("alt")
        var id = img.parentNode.getAttribute("href").split('id=')[1]
        item.innerHTML+= '<a href="'+"mpv://id="+id+'" class="button">open in mpv</a>'
})
};