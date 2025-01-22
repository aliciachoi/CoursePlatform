# Course Platform

## Overview
* A comprehensive video course platform built with Python and Django, enabling content creators to host and manage video-based courses with email verification and premium content access control.
* Features Cloudinary integration for optimized image and video hosting, along with a tailored user experience through TailwindCSS and HTMX.

## Features
* Video Course Management: Easily upload, organize, and manage video-based courses with customizable thumbnails and ordering.
* Email Verification System: Custom-built email verification workflow ensuring content access only to verified users.
* Dynamic Content Loading: HTMX integration for smooth, dynamic form handling and content updates without page refreshes.
* Advanced Video Playback: Cloudinary video player integration with adaptive streaming and automatic video resizing.
* Admin Dashboard: Customized Django admin interface for efficient course and lesson management.
* Responsive Design: Modern, responsive interface built with TailwindCSS and Flowbite components.
* Image Optimization: Automatic image resizing and optimization through Cloudinary integration.

## Technologies
* Frontend: HTML, TailwindCSS, HTMX, Flowbite
* Backend: Python 3.12, Django 5
* Media Storage: Cloudinary
* Email Service: Gmail SMTP
* Image Processing: Pillow
* CSS Framework: django-tailwind
* Authentication: Custom email verification system

## Key Components
* CloudinaryField integration for optimized media handling
* Custom model methods for different image sizes
* Reusable helper functions for Cloudinary operations
* Foreign key relationships for course-lesson structure
* Session-based email verification system
* HTMX-driven dynamic form handling
