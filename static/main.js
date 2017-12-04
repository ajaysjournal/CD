// const API_END_POINT = "http://localhost:8001/";
//
//

// developer notes
// todo move this JS to seperate file for code readability
const API_END_POINT = "/save";


$(document).ready(function () {
    rationales = []

    $('#save').on("submit", function (e) {
        e.preventDefault(); // cancel the actual submit
        console.log("save clicked")
        rationales.push($("input[name=labelme]:checked").map(function () {
             return $(this).attr("value");
        }).get());


        send_obj = {
            oid: $('#object_id').attr("value"),
            rationales: rationales[0]
        }
        $.ajax({
            type: "POST",
            url: API_END_POINT,
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(send_obj),
            success: function () {
                console.log("saved ", rationales)
                window.location.href = "/thankyou";
            }
        });
    });
});
