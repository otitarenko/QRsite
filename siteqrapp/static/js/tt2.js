
  var video = document.querySelector("#video");

  if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({video: true,
        facingMode: {
      exact: 'environment'}
    })
        .then(function (stream) {
          video.srcObject = stream;
        })
        .catch(function (err0r) {
          console.log("Something went wrong!");
        });
  }


      // let scanner = new Instascan.Scanner({ video: document.getElementById('preview') });
      // scanner.addListener('scan', function (content, image) {
      //   console.log(content);
      // });
      //
      // Instascan.Camera.getCameras().then(function (cameras) {
      //   if (cameras.length > 0) {
      //     scanner.start(cameras[0]);
      //   }
      // });






function capture() {
  var canvas = document.getElementById('canvas');
  var video = document.getElementById('video');

  canvas.width = 400;
  canvas.height = 600;
  canvas.getContext('2d').drawImage(video, 0, 0, 400,600);

  document.getElementById("printresult").innerHTML = canvas.toDataURL();
}
