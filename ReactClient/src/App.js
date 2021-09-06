import './App.css'
import axios from 'axios'
import {useState} from 'react'

function App() {

  const [file, setFile] = useState(null)

  const handleChange = event => {
    setFile(event.target.files[0])
  }

  const handleSubmit = () => {
    const formData = new FormData()
    formData.append("imageUpload", file, file.name)
    axios.post('upload_file', formData)
  }

  return (
    <div className="App">
      <div>
        <input type="file" onChange={handleChange} />
        <button onClick={handleSubmit}>
          Upload!
        </button>
      </div>
    </div>
  );
}

export default App;
