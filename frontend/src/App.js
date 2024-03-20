import { useEffect, useState } from 'react';
import './App.css';
import SearchForm from './components/SearchForm';
import Header from './components/Header';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {

  return (
    <div className="App">
      <Header />
      <div className='container'>

        <div className='cardWrapper'>
          <SearchForm />
        </div>
      </div>
      <ToastContainer />
    </div>
  );
}

export default App;
