#include <GL/glut.h>
#include <stdlib.h>
void init(void)
{
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glShadeModel(GL_FLAT);
}
void myInit()
{
    glMatrixMode(GL_PROJECTION); // set the view volume shape
    glLoadIdentity();
    // glOrtho(left, right, bottom, top, near, far)
    glOrtho(-5.0, 5.0, -5.0, 5.0, -0.1, 100);
    glMatrixMode(GL_MODELVIEW); // posicionar y apuntar la camara
    glLoadIdentity();
    gluLookAt(2.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
    glClear(GL_COLOR_BUFFER_BIT); // clear the screen
    glColor3d(0, 0, 0);           // draw black lines
}
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0, 1.0, 1.0);
    glPushMatrix();
    glTranslated(0.5, 0.5, 0.5);
    glutWireCube(4.0);
    glPopMatrix();
    glFlush();
}
void reshape(int w, int h)
{
    glViewport(0, 0, (GLsizei)w, (GLsizei)h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-10, 10, -10, 10, 0.5, 20);
    glMatrixMode(GL_MODELVIEW);
}
void keyboard(unsigned char key, int x, int y)
{
    switch (key)
    {
    case 'x':
    case 'X':
        glRotatef(30., 1.0, 0.0, 0.0);
        glutPostRedisplay();
        break;
    case 'y':
    case 'Y':
        glRotatef(30., 0.0, 1.0, 0.0);
        glutPostRedisplay();
        break;
    case 'i':
    case 'I':
        glLoadIdentity();
        gluLookAt(1, 1, 1, 0, 0, 0, 0, 1, 0);
        glutPostRedisplay();
        break;
    case 's':
    case 'S':
        glScaled(0.5, 0.5, 0.5);
        glutPostRedisplay();
        break;
    case 27:
        exit(0);
        break;
    }
}
int main(int argc, char **argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(640, 480);
    glutInitWindowPosition(100, 100);
    glutCreateWindow(argv[0]);
    glViewport(0, 0, 640, 480);
    init();
    myInit();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
    return 0;
}

// g++ -m32 -Wall -o 1.out 1.cpp -L"C:\MinGW\lib" -lglu32 -lglut32 -lopengl32 -lstdc++
