import React from 'react'
import { Link } from 'react-router-dom'

export default function HomePage() {
  return (
    <div className='container container-fluid'>
        <h2 style={{marginBottom: '2rem'}}>Diffie Hellman Key Exchange Algorithm</h2>
        <ul>
            <li>Alice - <Link to="/alice">Link</Link></li>
            <li>Bob - <Link to="/bob">Link</Link></li>
            <li>Eve - <Link to="/eve">Link</Link></li>
        </ul>
    </div>
  )
}
