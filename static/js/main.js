function toggleNav() {
    const navbarLinks = document.getElementById("navbar-links");
    navbarLinks.style.display = navbarLinks.style.display === "flex" ? "none" : "flex";
}

document.querySelectorAll('.video-containerr video').forEach(vid => {
    vid.onclick = () => {
        document.querySelector('.popup-video video').src = vid.getAttribute('src');
        document.querySelector('.popup-video video').removeAttribute('muted'); // Remove muted attribute
        document.querySelector('.popup-video').style.display = 'block';
    }
});

document.querySelector('.popup-video span').onclick = () =>{
    document.querySelector('.popup-video').style.display = 'none';
    document.querySelector('.popup-video video').muted=true; // Set muted attribute
    document.querySelector('.popup-video video').pause(); // Set muted attribute
    // let vid = document.getElementById("video1");
    // vid.muted = true; 
}
