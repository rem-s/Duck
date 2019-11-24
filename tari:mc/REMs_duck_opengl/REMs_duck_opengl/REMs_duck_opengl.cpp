// REMs_duck_opengl.cpp : このファイルには 'main' 関数が含まれています。プログラム実行の開始と終了がそこで行われます。
//

/* Shinchoku Base (ASUS MB at my home)
 * Intel Core i5 2400 , 8GB , NVIDIA GEFORCE GTX 650 Ti
 * Shinchoku Lab (Inspiron 570 at Lab)
 * AMD Athlon X2 240 , 8GB , AMD RADEON HD4850 
 * Shinchoku Mobile (MacBook Pro Late 2016)
 * Intel Core i5 6267U , 8GB , Intel Iris Graphics 550
 * Environment
 * Visual Studio 2017 on Windows 10
 */

#include "pch.h"
#include <iostream>
#include <GL/glut.h>

//prototype declarelation
//void draw_circle(float);
void draw_flag_th(void);
void draw_flag_ja(void);
void motion(float, float);

//global valiable

GLdouble normal[][3];
GLdouble vertex[][3][3]; //no,point123,xyz
int numQtySurface;//move to other cpp source file

const int HEIGHT_WINDOW = 300;
const int WIDTH_WINDOW = 300;

static GLfloat lightPosition[4] = {-20.0, -20.0, 100.0, 1.0};
static GLfloat lightDiffuse[3] = {1.0, 1.0, 1.0};
static GLfloat lightAmbient[3] = {0.25, 0.25, 0.25};
static GLfloat lightSpecular[3] = {1.0, 1.0, 1.0};

// status flag

int STATUS_MODE1 = 0;
int STATUS_MODE2 = 0;
int STATUS_MODE3 = 0;
int STATUS_MODE4 = 0;
int STATUS_MODE5 = 0;

//define colour at 8 bit array[3] = { R , G , B };

const GLfloat COLOUR_RED_FLAG_THA[3] = {237.0f / 255.0f, 046.0f / 255.0f, 056.0f / 255.0f};
const GLfloat COLOUR_BLUE_FLAG_THA[3] = {000.0f / 000.0f, 032.0f / 255.0f, 091.0f / 255.0f};
const GLfloat COLOUR_RED_FLAG_JPN[3] = {196.0f / 255.0f, 026.0f / 255.0f, 065.0f / 255.0f};
const GLfloat COLOUR_WHITE_COMMON[3] = {255.0f / 255.0f, 255.0f / 255.0f, 255.0f / 255.0f};

//const GLfloat COLOUR_WHITE_COMMON[3] = { 255.0f / 255.0f , 255.0f / 255.0f , 255.0f / 255.0f };

void drawCircle(float r)
{
	glBegin(GL_POLYGON); //polygon mode
	for (float x = -r; x <= r; x += r / 1000)
	{ //x^2 + y^2 = r^2 r = radius
		float y = sqrtf(r * r - x * x);
		glVertex2f(x, y); //draw 2d
	}
	for (float x = r; x >= -r; x -= r / 1000)
	{
		float y = sqrtf(r * r - x * x);
		y *= -1;
		glVertex2f(x, y);
	}
	glEnd();
	glFlush();
}
void drawFlagThai(void)
{
	std::cout << "DISPLAY NATIONAL FLAG OF THAI\n";
	glClear(GL_COLOR_BUFFER_BIT);
	float b1 = 2.0 / 3.0;
	float b2 = 1.0 / 3.0;
	float b3 = -1.0 * b2;
	float b4 = -1.0 * b1;
	glColor3fv(COLOUR_RED_FLAG_THA);
	glBegin(GL_POLYGON);
	glVertex2f(-1, 1);
	glVertex2f(1, 1);
	glVertex2f(1, b1);
	glVertex2f(-1, b1);
	glEnd();
	glColor3fv(COLOUR_BLUE_FLAG_THA);
	glBegin(GL_POLYGON);
	glVertex2f(-1, b2);
	glVertex2f(1, b2);
	glVertex2f(1, b3);
	glVertex2f(-1, b3);
	glEnd();
	glColor3fv(COLOUR_RED_FLAG_THA);
	glBegin(GL_POLYGON);
	glVertex2f(-1, b4);
	glVertex2f(1, b4);
	glVertex2f(1, -1);
	glVertex2f(-1, -1);
	glEnd();
	glFlush();
}

void drawFlagJapan(void)
{
	std::cout << "DISPLAY NATIONAL FLAG OF JAPAN\n";
	glClear(GL_COLOR_BUFFER_BIT);
	float r = 0.6f;
	glColor3fv(COLOUR_RED_FLAG_JPN);
	//glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, );
	glNormal3f(3, 0, -2);
	glBegin(GL_POLYGON); //polygon mode
	for (float x = -r; x <= r; x += r / 100000.0)
	{ //x^2 + y^2 = r^2 r = radius
		float y = sqrtf(r * r - x * x);
		float high_x = x * (2.0 / 3.0);
		glVertex3f(high_x, 0.2, y); //draw 2d
		glVertex3f(high_x, -0.2, y);
	}
	for (float x = r; x >= -r; x -= r / 100000.0)
	{
		float y = sqrtf(r * r - x * x);
		y *= -1;
		float high_x = x * (2.0 / 3.0);
		glVertex3f(high_x, 0.2, y);
		glVertex3f(high_x, -0.2, y);
	}
	glEnd();
	glFlush();
}

void motion(int x, int y)
{
	std::cout << "Motion\n";
	static float high_x_m = x;
	static float high_y_m = y;
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glPushMatrix();

	float dx, dy;
	dx = high_x_m - x;
	dy = high_y_m - y;
	glTranslatef(dx / 1.0, dy / 1.0, 0);
	glFlush();
	high_x_m = x;
	high_y_m = y;
	glPopMatrix();
}

void display(void)
{
	glLightfv(GL_LIGHT0, GL_POSITION, lightPosition);
	glLightfv(GL_LIGHT0, GL_DIFFUSE, lightDiffuse);
	glLightfv(GL_LIGHT0, GL_AMBIENT, lightAmbient);
	glLightfv(GL_LIGHT0, GL_SPECULAR, lightSpecular);

	std::cout << "MODE: ";
	std::cout << STATUS_MODE1;
	std::cout << "\n";
	switch (STATUS_MODE1)
	{
	case 1:
		drawFlagThai();
		break;
	case 2:
		drawFlagJapan();
		break;
	case 3:
		drawCircle(0.6);
		break;
	default:
		break;
	}
	//glClear(GL_COLOR_BUFFER_BIT);//fill colour buffer
	//for () {
	glRotated(2.0, 0.0, 1.0, 0.0);
	//}

	glColor3f(1.0, 0.3, 0.3); //green
	glFlush();				  //do remaining task
}
void init(void)
{
	glClearColor(1.0, 1.0, 1.0, 1.0); //window colour white
	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);
}

void keyboard(unsigned char key, int x, int y)
{
	switch (key)
	{
	case 't':
	case 'T':
		drawFlagThai();
		STATUS_MODE1 = 1;
		break;
	case 'j':
	case 'J':
		drawFlagJapan();
		STATUS_MODE1 = 2;
		break;
	default:
		break;
	}
	glFlush();
}

//DEVELOP

void displaySTL()
{
	int count;
	//normal -> stl
	for (count = 0 ; count <= numQtySurface)
	{
		glNormal3dv(normal[count]);
		glVertex3dv(vertex[count][1]);
		glVertex3dv(vertex[count][2]);
		glVertex3dv(vertex[count][3]);
	}
}

//END DEV

int main(int argc, char *argv[])
{
	std::cout << "Simulation\n";
	glutInit(&argc, argv);			//init glut
	glutInitDisplayMode(GLUT_RGBA); //colour mode is RGBA
	glutInitWindowSize(1200, 800);
	//gluPerspective(30.0, 900.0 / 600.0, 1.0, 100.0);
	glutCreateWindow(argv[0]); //Create window at argv[0]

	glutDisplayFunc(display); //call "display" function

	glutKeyboardFunc(keyboard);
	//glutMotionFunc(motion);

	init();

	glutMainLoop(); //infinite loop
	return 0;
}

// プログラムの実行: Ctrl + F5 または [デバッグ] > [デバッグなしで開始] メニュー
// プログラムのデバッグ: F5 または [デバッグ] > [デバッグの開始] メニュー

// 作業を開始するためのヒント:
//    1. ソリューション エクスプローラー ウィンドウを使用してファイルを追加/管理します
//   2. チーム エクスプローラー ウィンドウを使用してソース管理に接続します
//   3. 出力ウィンドウを使用して、ビルド出力とその他のメッセージを表示します
//   4. エラー一覧ウィンドウを使用してエラーを表示します
//   5. [プロジェクト] > [新しい項目の追加] と移動して新しいコード ファイルを作成するか、[プロジェクト] > [既存の項目の追加] と移動して既存のコード ファイルをプロジェクトに追加します
//   6. 後ほどこのプロジェクトを再び開く場合、[ファイル] > [開く] > [プロジェクト] と移動して .sln ファイルを選択します
