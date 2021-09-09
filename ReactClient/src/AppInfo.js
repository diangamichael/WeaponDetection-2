
export default function AppInfo() {
    return (
        <div id='info-main-div'>
            <h1>How does it work?</h1>
            <hr></hr>
            <p>1. The application sends your image to a server (a computer somewhere in the cloud).</p>
            <p>2. The server feeds the image to an Object Detection Model (Machine Learning).</p>
            <p>3. Once the image has been proccessed by the Model, it sends the result image to cloud storage (Amazon S3).</p>
            <p>4. Once the application receives confirmation that the result is ready, it grabs that image from cloud storage and
                  displays the result.</p>
        </div>
    )
}