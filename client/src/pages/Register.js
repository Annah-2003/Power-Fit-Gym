import React, { useEffect, useState } from 'react';
import RegiForm from '../components/RegiForm';

function Register() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("/users")
      .then((res) => res.json())
      .then((users) => setUsers(users));
  }, [users]);

  return (
    <>
      <div className="register">
        <h2>Register To Be Enrolled</h2>
        <RegiForm />
      </div>
    </>
  );
}

export default Register;
