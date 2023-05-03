import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { LoginView } from './views/LoginView';
import { HomeView } from './views/HomeView';
import { SessionDetailsView } from './views/SessionDetailsView';

const router = createBrowserRouter([
  {
    path: "/",
    element: <HomeView />,
  },
  {
    path: "login",
    element: <LoginView />,
  },
  {
    path: "sessions/:sessionId",
    element: <SessionDetailsView />
  },
]);

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
);
