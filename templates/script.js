"user strict";
window.onload = () => {

    var res = document.getElementById("res").value;

    res.onchange = () => {
        var widHt = [];
        switch(res) {
            case "pcSmall":
                widHt = [1024, 768];
                break;
            case "pcMedium":
                widHt = [1280, 1024];
                break;
            case "pcLarge":
                widHt = [1920, 1080];
                break;
            case "phoneSmall":
                widHt = [320, 480];
            case "phoneMed":
                widHt = [640, 960];
                break;
            case "phoneLarge":
                widHt = [1240, 1920];
        }

        document.getElementById("wid").value = widHt[0];
        console.log(document.getElementById("wid").value);
        document.getElementById("ht").value = widHt[1];
    }
}