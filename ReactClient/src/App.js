import './App.css'
import axios from 'axios'
import {useState} from 'react'

function App() {

  const [file, setFile] = useState(null)
  const [imageId, setImageId] = useState('')
  const [renderImage, setRenderImage] = useState(false)

  const handleChange = event => {
    setRenderImage(false)
    setFile(event.target.files[0])
  }

  const handleSubmit = async() => {
    const formData = new FormData()
    formData.append("imageUpload", file, file.name)
    try {
      const res = await axios.post('upload_file', formData)
      if (res.data.result === 'success') {
        setImageId(res.data.imageId)
        setRenderImage(true)
      }
    } catch(er) { console.log(er)}
  }

  return (
    <div className="App">
      <div>
        <input type="file" onChange={handleChange} />
        <button onClick={handleSubmit}>
          Upload!
        </button>
      </div>
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
