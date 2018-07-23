/*display entry form*/
function entry(){
	document.getElementById("new-entry").style.display='block';
	document.getElementById("view-entry").style.display='none';
}
/*display Posted  posts*/
function post(){
	document.getElementById("view-entry").style.display='block';
	document.getElementById("new-entry").style.display='none';
	//alert('cllc');
}