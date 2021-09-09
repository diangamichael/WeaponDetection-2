import axios from 'axios'
import {useState} from 'react'
import Button from 'react-bootstrap/Button'
import Spinner from 'react-bootstrap/Spinner'

export default function Home() {

    // state objects
  const [file, setFile] = useState(null)
  const [imageId, setImageId] = useState('')
  const [renderImage, setRenderImage] = useState(false)
  const [loading, setLoading] = useState(false)

  // sets file in state
  const handleChange = event => {
    setRenderImage(false)
    setFile(event.target.files[0])
  }

  // submits file to api
  const handleSubmit = async() => {
    // make sure file was received by input
    if (file === undefined || file === null) return
    setRenderImage(false)
    setLoading(true)
    const formData = new FormData()
    formData.append("imageUpload", file, file.name)
    try {
      const res = await axios.post('https://flask-service.e0db4cmami9tu.us-east-1.cs.amazonlightsail.com/upload_file', formData)
      if (res.data.result === 'success') {
        // response will include id of result image to pull from s3 bucket
        setImageId(res.data.imageId)
        setRenderImage(true)
        setLoading(false)
      }
    } catch(er) { console.log(er)}
  }

    return(
        <div>
            <div id='upload-form'>
                <h5>Upload an image to analyze</h5>
                <input type="file" onChange={handleChange} />
                <br></br>
                <Button variant="primary" onClick={handleSubmit}>Analyze</Button>{' '}
            </div>
        {
            loading ? 
            <div id='loading-spinner'>
                <h1 id='analysis-header'>Analyzing...</h1>
                <Spinner animation="border" role="status">
                <span className="visually-hidden">Loading...</span>
                </Spinner>
            </div>
            : null
        }
            <div>
                {
                renderImage ? 
                <div id='result-div'>
                    <img alt='result' id='result-image' src={`https://afarhidevgeneraldata.s3.amazonaws.com/latest_result_${imageId}`}/> 
                </div>
                : null
                }
            </div>
        </div>
    )
}