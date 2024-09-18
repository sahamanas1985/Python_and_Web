
function DisplayToastMessage(message, type)
{
    if(type == null) type="Normal";
    else if (type.toLowerCase() == "info") type="Info";
    else if (type.toLowerCase() == "success") type="Success";
    else if (type.toLowerCase() == "error") type="Error";
    else if (type.toLowerCase() == "warning") type="Warning";
    else type="Normal";

    new Toast(message, type).show();
}

function Toast(description, title) {
    
    var toastElement = buildToast(title, description);
    var toastWrapper = getOrCreateToastWrapper();
    toastWrapper.append(toastElement);
    this.bootstrapToast = bootstrap.Toast.getOrCreateInstance(toastElement);
    
    this.show = function() {
        this.bootstrapToast.show();
    }
    
    this.hide = function() {
        this.bootstrapToast.hide();
    }
    
    this.dispose = function() {
        this.bootstrapToast.dispose();
    }
}


function getOrCreateToastWrapper() {
    var toastWrapper = document.querySelector('body > [data-toast-wrapper]');
    
    if (!toastWrapper) {
        toastWrapper = document.createElement('div');
        toastWrapper.style.zIndex = 11;
        toastWrapper.style.position = 'fixed';
        toastWrapper.style.top = 0;
        toastWrapper.style.right = 0;
        toastWrapper.style.padding = '1rem';
        toastWrapper.setAttribute('data-toast-wrapper', ''); 
        document.body.append(toastWrapper);
    }
    
    return toastWrapper;
}

function buildToastBody(description, title) {
    var toastBody = document.createElement('div');
    toastBody.setAttribute('class', 'toast-body');
       
    
    if(title == "Normal") toastBody.setAttribute('style', 'color: #2471A3;');
    else if(title == "Warning") toastBody.setAttribute('style', 'color: black;');
    else toastBody.setAttribute('style', 'color: white;');

    var displayText = document.createElement('span');
    displayText.textContent = description;
    displayText.setAttribute('style', 'padding-left: 5px');
    
    var closeButton = document.createElement('button');
    closeButton.setAttribute('type', 'button');

    if(title == "Normal" || title=="Warning") closeButton.setAttribute('class', 'btn-close btn-close');
    else closeButton.setAttribute('class', 'btn-close btn-close-white');

    closeButton.setAttribute('data-bs-dismiss', 'toast');
    closeButton.setAttribute('data-label', 'Close'); 
    closeButton.setAttribute('style', 'float:right; opacity:0.8;');     

    var icon = document.createElement("i");
    icon.setAttribute('style', 'float: left; font-size: 20px; margin-top: -5px; padding-right: 3px');

    if(title == "Normal") icon.setAttribute('class', 'bi bi-chat-dots-fill'); 
    else if(title == "Info") icon.setAttribute('class', 'bi bi-chat-dots-fill'); 
    if(title == "Success") icon.setAttribute('class', 'bi-check-circle-fill');  
    if(title == "Warning") icon.setAttribute('class', 'bi bi-exclamation-circle-fill'); 
    if(title == "Error") icon.setAttribute('class', 'bi bi-exclamation-circle-fill'); 

    toastBody.append(icon);
    toastBody.append(displayText);
    toastBody.append(closeButton);
    
    return toastBody;
}

function buildToast(title, description) {
    var toast = document.createElement('div');
    toast.setAttribute('class', 'toast');
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
           
    if(title == "Info") toast.setAttribute('style', 'background-color: #3498DB; border-radius: 8px');
    else if(title == "Success") toast.setAttribute('style', 'background-color: #28B463; border-radius: 8px');
    else if(title == "Error") toast.setAttribute('style', 'background-color: #E74C3C; border-radius: 8px');
    else if(title == "Warning") toast.setAttribute('style', 'background-color: #FFDC2E; border-radius: 8px');
    else toast.setAttribute('style', 'background-color: white; border-radius: 8px');
      
    var toastBody = buildToastBody(description, title);
      
    toast.append(toastBody);
    
    return toast;
}