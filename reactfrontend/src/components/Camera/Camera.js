import axios from 'axios'; 
import React, { useState } from 'react';
import Camera, { FACING_MODES, IMAGE_TYPES, ImagePreview } from 'react-html5-camera-photo';
import 'react-html5-camera-photo/build/css/index.css';
 
function UseCamera(props) {
  const [dataUri, setDataUri] = useState('');

  function handleTakePhoto (dataUri) {
    // Do stuff with the photo...
    axios.post("http://localhost:5000/api/upload", dataUri);
    console.log('takePhoto');
  }

  function handleTakePhotoAnimationDone (dataUri) {
    // Do stuff with the photo...
    console.log('takePhoto');
    setDataUri(dataUri);
  }
 
  function handleCameraError (error) {
    console.log('handleCameraError', error);
  }
 
  function handleCameraStart (stream) {
    console.log('handleCameraStart');
  }
 
  function handleCameraStop () {
    console.log('handleCameraStop');
  }
 
  const isFullscreen = false;

  return (
      <div>
        <Camera
            onTakePhoto = { (dataUri) => { handleTakePhoto(dataUri); } }
            onTakePhotoAnimationDone = { (dataUri) => { handleTakePhotoAnimationDone(dataUri); } }
            onCameraError = { (error) => { handleCameraError(error); } }
            idealFacingMode = {FACING_MODES.ENVIRONMENT}
            idealResolution = {{width: 640, height: 480}}
            imageType = {IMAGE_TYPES.JPG}
            imageCompression = {0.97}
            isMaxResolution = {true}
            isImageMirror = {false}
            isSilentMode = {false}
            isDisplayStartCameraError = {true}
            isFullscreen = {false}
            sizeFactor = {1}
            onCameraStart = { (stream) => { handleCameraStart(stream); } }
            onCameraStop = { () => { handleCameraStop(); } }
        />
        <img src={dataUri} width="500" height="300" />
    </div>
  );
}
 
export default UseCamera;