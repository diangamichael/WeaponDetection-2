import './App.css'
import axios from 'axios'
import {useState} from 'react'

function App() {

  const [file, setFile] = useState(null)
  const [img, setImg] = useState(null)

  const handleChange = event => {
    setFile(event.target.files[0])
  }

  const handleSubmit = async() => {
    const formData = new FormData()
    formData.append("imageUpload", file, file.name)
    try {
      const res = await axios.post('upload_file', formData)
      setImg(res.data)
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
        {img ? 
          <div>
            <p>Here is an image</p>
            <img src={img}/> 
          </div>
          
        : ''}
      </div>
    </div>
  );
}

export default App;
