function reBuild(addrList) {
    $("table").children("tbody").html(addrList)

}



function filter() {
    var addr = $("#addr").val()
    addr = addr.trim().toString();


    var addrList = []
    var temp = $("table").children("tbody").children("tr").each(
        function () {
            var t1 = $(this).children("td:eq(7)").text()
            if (addr == t1 || t1.search(addr) != -1) {
                addrList.push(this)
            }
        }
    );
    if (addrList) {
        reBuild(addrList);
        console.log("success")
    } else {
        alert("没有符合条件的地址")
        console.log("fail")
    }
    console.log(addrList)

}
