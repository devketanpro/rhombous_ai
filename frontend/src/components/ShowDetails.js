import React, { useState, useEffect } from 'react';
import { DataGrid } from '@mui/x-data-grid';

const MUIDataGridComponent = () => {
  // State to store data fetched from the API
  const [rows, setRows] = useState([]);
  const [columns, setColumns] = useState([{ field: 'id', headerName: 'ID', width: 100 }]);

  useEffect(() => {
    // Fetch data from the API
    fetch('http://0.0.0.0:8000/data')
      .then(response => response.json())
      .then(data => {
        // Update the state with the fetched data
        setRows(data.records.map((row) => {
          return {id: row.id, Name: row.name, Birthdate: row.birthdate, Score: row.score, Grade: row.grade}
        }));

        setColumns(data.columns.map((col) => {
          return {field: col.name, headerName: `${col.name} - ${col.data_type}`, width: 200}
        }))
      })
      .catch(error => {
        console.error('Error fetching data:');
      });
  }, []); // Empty dependency array to ensure the effect runs only once

  return (
    <div style={{ height: 400, width: '100%' }}>
      {
        rows.length > 0 && <DataGrid rows={rows} columns={columns} pageSize={5} /> 
      }
    </div>
  );
};

export default MUIDataGridComponent;
