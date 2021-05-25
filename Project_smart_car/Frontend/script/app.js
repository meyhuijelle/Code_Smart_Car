const lanIP = `${window.location.hostname}:5000`;
const socket = io(`http://${lanIP}`);



const showHistoriek = function(jsonObject){
  console.log(jsonObject)
//   let htmlString = `<tr>
//   <th>HistoriekID</th>
//   <th>DeviceID</th>
//   <th>ActieID</th>
//   <th>Actiedatum</th>
//   <th>Waarde</th>
//   <th>Commentaar</th>
// </tr>`
let htmlString = `` 
  const placeholder = document.querySelector('.js-historiek')
  for(historiek of jsonObject.historiek){
    console.log(historiek)
    // htmlString += `<li class="js-historiek_option">ID: ${historiek.ActieID} ActieDatum: ${historiek.Actiedatum} kies</li>`
    htmlString += ` <tr>
    <td>ID: ${historiek.ActieID} --- Actiedatum: ${historiek.Actiedatum} --- Commentaar: ${historiek.Commentaar} --- DeviceID: ${historiek.DeviceID} --- HistoriekID: ${historiek.HistoriekID} </td>
    </tr>`

    
  }
  placeholder.innerHTML = htmlString

}

const getHistoriek = function(){
  handleData(`http://192.168.168.168:5000/api/v1/historiek`, showHistoriek)
}

const listenToUI = function () {
  
};

const listenToSocket = function () {
  socket.on("connect", function () {
    console.log("verbonden met socket webserver");
  });

  

  socket.on('B2F_verstuur_data', function(jsonObject){
    let today = new Date();
    // console.log('Ik ben er')
    console.log(jsonObject)
    document.querySelector('.js-data').innerHTML = `De lichtsterkte van de LDR is: ${jsonObject.data}%`
    const object = {
      DeviceID: 3,
      ActieID: 2,
      Actiedatum: '2017-05-31 19:19:09',
      // Actiedatum: today,
      Waarde: 33.5,
      Commentaar: "Dit is voorbeeldcommentaar "
    }
    console.log('Dit is het object')
    console.log(object)
    handleData(`http://192.168.168.168:5000/api/v1/historiek`, null, null, 'POST', JSON.stringify(object))
  }) 

};

document.addEventListener("DOMContentLoaded", function () {
  console.info("DOM geladen");
  listenToUI();
  listenToSocket();
  getHistoriek();
});
