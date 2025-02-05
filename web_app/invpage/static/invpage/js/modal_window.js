function openModal(itemName, maxQuantity) {
    document.getElementById('modal-item-name').value = itemName;
    document.getElementById('modal-quantity').setAttribute('max', maxQuantity);
    document.getElementById('myModal').style.display = "block";
}

function closeModal() {
    document.getElementById('myModal').style.display = "none";
}

window.onclick = function(event) {
    var modal = document.getElementById('myModal');
    if (event.target == modal) {
        modal.style.display = "none";
    }
}