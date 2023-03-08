

window.onload=function(){
    var files = [];
    const selected_file = document.querySelector('.selected_file'),
    image_upload = document.querySelector('.image_upload'),
    text = document.querySelector('.inner'),
    browse = document.querySelector('.select'),
    uploadFile = document.querySelector('.file');

    browse.addEventListener('click',() => uploadFile.click());

    uploadFile.addEventListener('change',()=>{
        let file = uploadFile.files;
        for(let i = 0; i < file.length; i++){
            if (files.every(e => e.name != file[i].name))
                files.push(file[i]);
        }
        let fileList = new DataTransfer();
        for(let i = 0; i < files.length; i++){
            fileList.items.add(files[i]);
        }

        uploadFile.files = fileList.files;

        showImages();
    })

    const showImages = () => {
        let images = '';
    
        files.forEach((e, i) => {
            images +=   `<div class="image">
                            <img src="${URL.createObjectURL(e)}" alt="image">
                            <span class="del-image" data-index="${i}">&times;</span>
                        </div>`;
        });
    
        selected_file.innerHTML = images;
    
        const delImageButtons = document.querySelectorAll('.del-image');
        delImageButtons.forEach(button => {
            button.addEventListener('click', () => {
                const index = button.getAttribute('data-index');
                files.splice(index, 1);
                list = new DataTransfer();
                for (let i = 0; i < files.length; i++) {
                    list.items.add(files[i]);
                }
                uploadFile.files = list.files;
                showImages();
            });
        });
    };

    //set button delete image
    const setupDelImgBtn = () =>{
        // if images list not empty
        if(typeof imageList !== 'undefined' && imageList.length > 0){
            const fetchPromises = [];
            var listFile = new DataTransfer();
            for (let i = 0; i < imageList.length; i++){
                fetchPromises.push(fetch(imageList[i]));
            }

            Promise.all(fetchPromises)
                .then(responses => Promise.all(responses.map(res => res.blob())))
                .then(blobs => {
                    for (let i = 0; i < blobs.length; i++){
                        const file = new File([blobs[i]], imageList[i].split('/').pop(), {type: 'image/jpeg'});
                        files.push(file);
                        listFile.items.add(file);
                    }
                })
                .then(() => {
                    showImages();
                    uploadFile.files = listFile.files;
                });
        }
    };

    setupDelImgBtn();


    image_upload.addEventListener('dragover', e => {
        e.preventDefault();
        image_upload.classList.add('dragover');
        text.innerHTML = 'Drop images here';
    })

    image_upload.addEventListener('dragleave', e => {
        e.preventDefault();
        image_upload.classList.remove('dragover');
        text.innerHTML = 'Drag & drop image here or <span class="select">Browser</span>';
    })

    image_upload.addEventListener('drop', e => {
        e.preventDefault();
        image_upload.classList.remove('dragover');
        text.innerHTML = 'Drag & drop image here or <span class="select">Browser</span>';
        let file = e.dataTransfer.files;
        for(let i = 0; i < file.length; i++){
            if (files.every(e => e.name != file[i].name));
                files.push(file[i]);
        }
        let fileList = new DataTransfer();
        for(let i = 0; i < files.length; i++){
            fileList.items.add(files[i]);
        }

        uploadFile.files = fileList.files;

        // selected_file.reset();
        showImages();
    })

    //display image get from django productImageForm
    // const displayImage = () =>{
    //     var images = JSON.parse('{{ productImages|escapejs }}');
    //     for(let i = 0; i < images.length; i++){
    //         files.push(images[i]);
    //     }
    //     showImages();
    // }
    // displayImage();

}
