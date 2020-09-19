# Blend4Web browser scene with embedded video stream

In this project I created a simple 3D scene with [**Blender**](https://www.blender.org/), converted it to WebGL by using the [**Blend4Web**](https://www.blend4web.com/) framework and finally connected and embedded a video stream (JPEG sequence in fact) from my Raspberry Pi Zero camera into the rendered scene.
The final visual result as well as detailed step-by-step tutorial can be found below in the **video tutorial** section.

## Video tutorial and result

<div align="left">
      <a href="https://www.youtube.com/watch?v=XkTMaYFVQbo">
         <img src="https://img.youtube.com/vi/XkTMaYFVQbo/0.jpg" style="width:100%;">
      </a>
</div>


## Files description
- [**cam_project/**](https://github.com/10ondr/Blend4Web-video-stream/tree/master/cam_project) - Blend4Web project ready to be deployed to a server.
- [**cam_project/build/cam_project.html**](https://github.com/10ondr/Blend4Web-video-stream/blob/master/cam_project/build/cam_project.html) - The entry point HTML page.
- [**cam_project/blender/**](https://github.com/10ondr/Blend4Web-video-stream/tree/master/cam_project/blender) - Blender project.
- [**web_server.py**](https://github.com/10ondr/Blend4Web-video-stream/blob/master/web_server.py) - Simple Python webserver for delivering the files and base64 encoded JPEGs.
