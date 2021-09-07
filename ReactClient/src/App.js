import './App.css'
import axios from 'axios'
import {useState} from 'react'
import NavigationBar from './NavigationBar'
import Button from 'react-bootstrap/Button'
import Spinner from 'react-bootstrap/Spinner'

function App() {

  const [file, setFile] = useState(null)
  const [imageId, setImageId] = useState('')
  const [renderImage, setRenderImage] = useState(false)
  const [loading, setLoading] = useState(false)

  const handleChange = event => {
    setRenderImage(false)
    setFile(event.target.files[0])
  }

  const handleSubmit = async() => {
    setLoading(true)
    const formData = new FormData()
    formData.append("imageUpload", file, file.name)
    try {
      const res = await axios.post('upload_file', formData)
      if (res.data.result === 'success') {
        setImageId(res.data.imageId)
        setRenderImage(true)
        setLoading(false)
      }
    } catch(er) { console.log(er)}
  }

  return (
    <div className="App">
      <NavigationBar />
      <div id='upload-form'>
        <input type="file" onChange={handleChange} />
        <br></br>
        <Button variant="primary" onClick={handleSubmit}>Submit</Button>{' '}
      </div>
      {
        loading ? 
        <div id='loading-spinner'>
          <Spinner animation="border" role="status">
            <span className="visually-hidden">Loading...</span>
          </Spinner>
        </div>
        : null
      }
      
      
      <div>
        {renderImage ? 
          <div>
            <p>Here is an image</p>
            <img src={`https://afarhidevgeneraldata.s3.amazonaws.com/latest_result_${imageId}`}/> 
          </div>
        : ''}
      </div>
    </div>
  );
}

export default App;
