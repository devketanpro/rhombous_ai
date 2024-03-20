import React, { useState } from 'react';
import { Button, Paper, Typography } from '@mui/material';
import axios from 'axios';
import ShowDetails from './ShowDetails';

const FileUploadComponent = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploading, setUploading] = useState(false);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleUpload = async () => {
    try {
      setUploading(true);
      const formData = new FormData();
      formData.append('file', selectedFile);
      const response = await axios.post('http://0.0.0.0:8000/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      console.log('File uploaded successfully:', response.data);
    } catch (error) {
      console.error('Error uploading file:', error);
    } finally {
      setUploading(false);
    }
  };

  return (
    <>
      <Paper elevation={3} style={{ padding: '20px', maxWidth: '400px', margin: 'auto', marginBottom: '50px'}}>
        <Typography variant="h5" gutterBottom>
          Upload File
        </Typography>
        <input
          type="file"
          accept=".csv,.xlsx,.xls"
          onChange={handleFileChange}
          style={{ marginBottom: '20px' }}
          />
        <Button
          variant="contained"
          color="primary"
          onClick={handleUpload}
          disabled={!selectedFile || uploading}
          >
          {uploading ? 'Uploading...' : 'Upload'}
        </Button>
      </Paper>
      {
        !uploading && <ShowDetails />
      }
    </>
  );
};

export default FileUploadComponent;
