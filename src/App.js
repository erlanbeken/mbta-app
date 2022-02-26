import React, { useState, useEffect } from 'react';
import Moment from 'react-moment';
import logo from './logo.svg';
import './App.css';

function App() {
    const [currentBoard, setCurrentBoard] = useState([]);
    useEffect(() => {
        fetch('/api/mbta_departure_board').then(res => res.json()).then(data => {
            setCurrentBoard(data['result']);
        });
      }, []);
    const today = new Date();
    return (
        <div className="App">
            <header className="App-header">
                <div className="current-date">
                    <div><Moment format="dddd">{today}</Moment></div>
                    <div><Moment format="DD/MM/YYYY">{today}</Moment></div>
                </div>
                <div className="header">North Station Information</div>
                <div className="current-time">
                    <div>Current time:</div>
                    <div><Moment format="h:mm a">{today}</Moment></div>
                </div>
            </header>
            <div className="departure-table">
                <table className="departure-board">
                    <thead>
                        <tr>
                            <td>Carrier</td>
                            <td>Time</td>
                            <td>Destination</td>
                            <td>Train #</td>
                            <td>Track #</td>
                            <td>Status</td>
                        </tr>
                    </thead>
                    <tbody>
                    {currentBoard.map((value, index) => {
                        return (
                            <tr key={index}>
                            <td>{value.carrier}</td>
                            <td>{value.time}</td>
                            <td>{value.destination}</td>
                            <td>{value.train}</td>
                            <td>{value.track}</td>
                            <td>{value.status}</td>
                           </tr>
                        );
                    })}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default App;
