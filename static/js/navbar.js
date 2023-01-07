for (const data of document.getElementsByTagName("a")) {
    if (data.href == document.URL){
        data.parentElement.classList.add("active")
    } 
}