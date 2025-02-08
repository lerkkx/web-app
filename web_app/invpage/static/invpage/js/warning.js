function openWarning(requestId) {
    console.log(requestId)
    document.getElementById('warningRequestId').value = requestId;
    document.getElementById('warning').style.display = 'flex';
}
function closeWarning() {
    document.getElementById('warning').style.display = "none";
}