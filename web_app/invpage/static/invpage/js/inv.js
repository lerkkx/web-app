function openNav() {
    document.getElementById("sidebar").style.left = "0";
    document.body.classList.add('blur');
}

function closeNav() {
    document.getElementById("sidebar").style.left = "-250px";
    document.body.classList.remove('blur');
}

function CButton() {
    const el = document.querySelector('.inventory-list');
    const styles = window.getComputedStyle(el);
    const fc = styles.maxHeight
    if (fc== '0px' ) {
        
        const mxH =  document.getElementById("inventory-list-good").scrollHeight;
        document.getElementById("inventory-list-good").style.maxHeight =  mxH  + "px";
    } else {
        document.getElementById("inventory-list-good").style.maxHeight =  "0px";
    }
}

const toggleButton = document.querySelector('.toggle-section .btnlist');

toggleButton.addEventListener('click', function() {
  this.classList.toggle('active');
});