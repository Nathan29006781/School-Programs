/*
Carina Gandhi
Aya Ahmed
Nathan Menezes
Emily DiLauro
CANE - A Loneliness Aid
Version 15.0
*/

const int X_LENGTH = 7;
const int Y_LENGTH = 6;
const tMotor GATE_PORT = motorA;
const tMotor MAG_PORT = motorB;
const tMotor SLIDE_PORT = motorC;
const tMotor LIFT_PORT = motorD;
const TLegoColors ROBOT_COLOUR = colorWhite;
const TLegoColors PLAYER_COLOUR = colorRed;
const TEV3Buttons SHUTDOWN_BUTTON = buttonBack;
const TTimers ABSENCE_TIMER = T1;
const TTimers NO_PLAY_TIMER = T2;
const int ABSENCE_TIMEOUT = 15000;
const int NO_PLAY_TIMEOUT = 2*ABSENCE_TIMEOUT;
const int RESULT_TIME = 5000;
const int COL_PORT = 1; //Port 2
const int US_PORT = 3; //Port 4
const int DELTA_X = 167;
const int DELTA_Y = 163;
const int MAG_RETURN = 20;

TLegoColors board[Y_LENGTH][X_LENGTH];
TLegoColors old_board[Y_LENGTH][X_LENGTH];
short score = 0;

void resetGate(bool closed = true);
void resetMotors();
void resetBoard(bool gateClosed = false);
void gateSet(bool closed = true, int speed = 15);
void moveX(float position, int speed = 30);
void moveY(float position, int speed = 30);
void moveXY(float x_position, float y_position, int speed = 60);
TEV3Buttons waitForPress(TEV3Buttons button1 = buttonEnter, TEV3Buttons button2 = buttonEnter);
void display(const string & text, bool big_text = true);
void displayBoard();
void displayOldBoard();
bool personThere();
bool updateBoard();
bool winner(TLegoColors colour);
void playerMove();
void robotMove();
short getScore();
void saveScore(short high_score);
bool playAgain();
void shutDown();

TLegoColors getColour();
char getColourChar(TLegoColors colour);

task main()
{
	clearDebugStream();
	setSoundVolume(100);
	setBlockBackButton(true);

	bool play_again = true;
	while(play_again)
	{
		resetBoard(true);

		display("Waiting for player...", false);
		setLEDColor(ledOrangePulse);
		resetTimer(ABSENCE_TIMER);
		while (!personThere())
		{
			if(time1[ABSENCE_TIMER]>ABSENCE_TIMEOUT || getButtonPress(SHUTDOWN_BUTTON)) shutDown();
		}
		playSoundFile("Hello.rsf");
		display("Press Enter to Start!", false);

		displayCenteredTextLine(8, "The high score is %d", getScore());
		waitForPress();

		bool player_turn = false;
		bool round_on = true;

		while (round_on)
		{
			if(player_turn)
			{
				playerMove();

				bool cheat = false;
				while(!cheat)
				{
					cheat = updateBoard();
					if(!cheat) break;
					else
					{
						display("You CHEATED");
						setLEDColor(ledRedPulse);
						playSoundFile("Shouting.rsf");
						wait1Msec(5000);
						if(getButtonPress(buttonLeft)) cheat = false;
						else
						{
							playSoundFile("Laughing 2.rsf");
							score = -100;
							wait1Msec(RESULT_TIME);
							round_on = false;
							play_again = false;
						}
					}
				}

				if (!cheat && winner(PLAYER_COLOUR))
				{
					display("You Won");
					setLEDColor(ledGreenFlash);
					playSoundFile("Cheering.rsf");
					score += 3;
					wait1Msec(2000);
					playSoundFile("Fanfare.rsf");
					wait1Msec(RESULT_TIME);
					round_on = false;
					play_again = playAgain();
				}
			}//end if player_turn

			else
			{
				robotMove();
				if(winner(ROBOT_COLOUR)) //Player lost
				{
					display("You Lost");
					setLEDColor(ledRedFlash);
					playSoundFile("Laughing 2.rsf");
					wait1Msec(2000);
					playSoundFile("Sorry.rsf"); //Score unchanged
					wait1Msec(RESULT_TIME);
					round_on = false;
					play_again = playAgain();
				}
			} // end robot move
			//check for draw
			bool draw = true;
			for(int row = 0; row < Y_LENGTH; row++)
			{
				for(int col = 0; col < X_LENGTH; col++)
				{
					if(draw && board[row][col] == colorNone)
					{
						draw = false;
					}
				}
			}
			if(draw)
			{
				display("Game Drawed");
				setLEDColor(ledOrangeFlash);
				playSoundFile("Uh-oh.rsf");
				score += 1;
				wait1Msec(RESULT_TIME);
				round_on = false;
				play_again = playAgain();
			}
			//end draw

			player_turn = !player_turn;
		}//end while round_on

	}//end while play_again
	shutDown();
}

//resets the gate at the bottom to allow pieces to fall out
void resetGate(bool closed)
{
	writeDebugStreamLine("Resetting Gate");
	const int START_SPEED = 15;
	const int STOP_RPM = 10;

	motor[GATE_PORT] = START_SPEED;

	wait1Msec(250);

	waitUntil(abs(getMotorRPM(GATE_PORT)) < STOP_RPM);
	motor[GATE_PORT] = 0;
	nMotorEncoder[GATE_PORT] = 0;
	if(closed)
	{
		wait1Msec(4000);
		gateSet(true, START_SPEED);
	}

	writeDebugStreamLine("Gate Reset");
}

//resets motors to bottom right corner
void resetMotors()
{
	const int NORMAL_START_SPEED = 40;
	const int FAST_START_SPEED = 100;
	const int STOP_RPM = 8;

	writeDebugStreamLine("Resetting Motors");
	if(-nMotorEncoder[SLIDE_PORT] > 150 && -nMotorEncoder[LIFT_PORT] > 150) moveXY(100, 100, 100);
	else if(-nMotorEncoder[SLIDE_PORT] > 150)
	{
		moveX(100, FAST_START_SPEED);
		motor[SLIDE_PORT] = 0;
	}
	else if(-nMotorEncoder[LIFT_PORT] > 150)
	{
		moveY(100, FAST_START_SPEED);
		motor[LIFT_PORT] = 0;
	}

	bool slide = true, lift = true;
	motor[SLIDE_PORT] = NORMAL_START_SPEED;
	motor[LIFT_PORT] = NORMAL_START_SPEED;

	wait1Msec(150);

	while(slide || lift){
		if(slide && abs(getMotorRPM(SLIDE_PORT)) < STOP_RPM){
			slide = false;
			motor[SLIDE_PORT] = nMotorEncoder[SLIDE_PORT] = 0;
		}
		if(lift && abs(getMotorRPM(LIFT_PORT)) < STOP_RPM){
			lift = false;
			motor[LIFT_PORT] = nMotorEncoder[LIFT_PORT] = 0;
		}
		if(getButtonPress(SHUTDOWN_BUTTON)) shutDown();
	}
	writeDebugStreamLine("Motors Reset");
}

//resets all systems and arrays
void resetBoard(bool gateClosed)
{
	display("Resetting Board...");
	setLEDColor(ledRedFlash);
	resetMotors();
	playSound(soundBeepBeep);
	resetGate(gateClosed);
	for(int row = 0; row < Y_LENGTH; row++){
		for(int col = 0; col < X_LENGTH; col++)
		{
			board[row][col] = colorNone;
			old_board[row][col] = colorNone;
		}
	}
	display("Board Reset Complete!", false);
	setLEDColor(ledGreenFlash);
	playSoundFile("Ready.rsf");
	wait1Msec(500);
}

void go(tMotor motor_index, int position = 0, int speed = 30)
{
	const int TOLERANCE = 5;

	//Actual encoders are in reversed orientation
	motor[motor_index] = sgn(-nMotorEncoder[motor_index]-position)*speed;
	if(-nMotorEncoder[motor_index] > position)
	{
		while(TOLERANCE < -(position+nMotorEncoder[motor_index]))
		{
			if(getButtonPress(SHUTDOWN_BUTTON)) shutDown();
		}
	}
	else if(-nMotorEncoder[motor_index] < position)
	{
		while(TOLERANCE < position+nMotorEncoder[motor_index])
		{
			if(getButtonPress(SHUTDOWN_BUTTON)) shutDown();
		}
	}
}

//opens or closes gate
void gateSet(bool closed, int speed)
{
	const int GATE_CLOSED = 175;
	go(GATE_PORT, closed ? GATE_CLOSED : 0, speed);
	motor[GATE_PORT] = 0;
}

//locks motor into magazine
void engageMag()
{
	writeDebugStreamLine("Engaging Magazine");
	if(-nMotorEncoder[LIFT_PORT] < 600 && -nMotorEncoder[SLIDE_PORT] > 100) moveXY(70, 670, 60);
	moveX(MAG_RETURN);
	motor[SLIDE_PORT] = 0;
	moveY(770, 50);
	motor[LIFT_PORT] = 0;
	writeDebugStreamLine("Magazine Engaged");
	wait1Msec(250);
}

void moveX(float position, int speed)
{
	if(position < 5) position = 10;
	else if(position > DELTA_X*(X_LENGTH-1)-20 && -nMotorEncoder[LIFT_PORT] > DELTA_Y*(Y_LENGTH-2)) position = 985;
	writeDebugStreamLine("Moving X to %d", position);
	go(SLIDE_PORT, position, speed);
	writeDebugStreamLine("X movement complete");
}

void moveY(float position, int speed)
{
	writeDebugStreamLine("Moving Y to %d", position);
	go(LIFT_PORT, position, speed);
	writeDebugStreamLine("Y movement complete");
}

//simultaneous movement of x and y motors
void moveXY(float x_position, float y_position, int speed)
{
	writeDebugStreamLine("Moving X to %d and Y to %d", x_position, y_position);
	const int TOLERANCE = 5;

	//Actual encoders are in reversed orientation
	motor[SLIDE_PORT] = sgn(-nMotorEncoder[SLIDE_PORT]-x_position)*speed;
	motor[LIFT_PORT] = sgn(-nMotorEncoder[LIFT_PORT]-y_position)*speed;
	bool slide = true, lift = true;
	while (slide || lift)
	{
		if (abs(x_position+nMotorEncoder[SLIDE_PORT]) <= TOLERANCE)
		{
			slide = false;
			motor[SLIDE_PORT]=0;
		}
		if (abs(y_position+nMotorEncoder[LIFT_PORT]) <= TOLERANCE)
		{
			lift = false;
			motor[LIFT_PORT]=0;
		}
	}
	motor[SLIDE_PORT]=motor[LIFT_PORT]=0;
	writeDebugStreamLine("XY movement complete");
}

//moves to desired playing position and plays the piece
void dropPiece(int x_coord)
{
	writeDebugStreamLine("Dropping Piece");
	if(-nMotorEncoder[LIFT_PORT] < 680) engageMag();
	moveX(x_coord*DELTA_X-15);
	motor[SLIDE_PORT] = 0;
	wait1Msec(500);


	nMotorEncoder[MAG_PORT] = 0;
	go(MAG_PORT, 70, 50);
	motor[MAG_PORT] = 0;
	writeDebugStreamLine("Reversed Magazine");

	wait1Msec(100);

	go(MAG_PORT, -20, 45);
	motor[MAG_PORT] = 0;
	writeDebugStreamLine("Magazine moved forward");
	wait1Msec(500);
	writeDebugStreamLine("Dropped Piece");

	wait1Msec(100);

	moveX(MAG_RETURN);
	motor[SLIDE_PORT] = 0;
}

//beeps while waiting for the user
TEV3Buttons waitForPress(TEV3Buttons button1, TEV3Buttons button2)
{
	waitUntil(!getButtonPress(buttonAny));
	time1[ABSENCE_TIMER]=0;
	time1[NO_PLAY_TIMER]=0;
	unsigned long beeped = nPgmTime, displayed = nPgmTime;
	while(true)
	{
		long time_remaining;
		if(getButtonPress(button1)) return button1;
		if(getButtonPress(button2)) return button2;
		if(personThere()){
			resetTimer(ABSENCE_TIMER);
			time_remaining = NO_PLAY_TIMEOUT-time1[NO_PLAY_TIMER];
		}
		else time_remaining = ABSENCE_TIMEOUT-time1[ABSENCE_TIMER];

		if(time1[NO_PLAY_TIMER]>NO_PLAY_TIMEOUT || time1[ABSENCE_TIMER]>ABSENCE_TIMEOUT || getButtonPress(SHUTDOWN_BUTTON)) shutDown();
		if(nPgmTime - displayed > 500)
		{
			const int LINE = 2;
			displayClearTextLine(LINE);
			displayCenteredBigTextLine(LINE, "Time Left: %d", (int)ceil(time_remaining/1000.0));
			displayed = nPgmTime;
		}
		const int FREQUENCY = 2000;
		if(time_remaining < 2000)
		{
			if(nPgmTime - beeped > 100)
			{
				playTone(FREQUENCY, 5);
				beeped = nPgmTime;
			}
		}
		else if(time_remaining < 7000)
		{
			if(nPgmTime - beeped > 500)
			{
				playTone(FREQUENCY, 5);
				beeped = nPgmTime;
			}
		}
		else if(time_remaining < 12000)
		{
			if(nPgmTime - beeped > 1000)
			{
				playTone(FREQUENCY, 5);
				beeped = nPgmTime;
			}
		}
	}
	return SHUTDOWN_BUTTON;
}

//scans colour and reads it out
TLegoColors getColour()
{
	TLegoColors colour = getColorName(COL_PORT);
	if(colour != PLAYER_COLOUR && colour != ROBOT_COLOUR)
	{
		colour = colorNone;
	}
	if(colour == colorRed) playSoundFile("Red.rsf");
	if(colour == colorWhite) playSoundFile("White.rsf");
	return colour;
}

//converts colour to text
char getColourChar(TLegoColors colour)
{
	switch(colour)
	{
	default:
		return 'O';
		break;
	case colorRed:
		return 'R';
		break;
	case colorWhite:
		return 'W';
		break;
		/*
		case colorYellow:
		return 'Y';
		break;
		case colorBlack:
		return 'B';
		break;
		*/
	}
}

void display(const string & text, bool big_text)
{
	const int LINE = 6;
	eraseDisplay();
	wait1Msec(100);
	if(big_text)
	{
		displayCenteredBigTextLine(LINE, text);
	}
	else
	{
		displayCenteredTextLine(LINE, text);
	}
	writeDebugStreamLine(text);
}

//outputs the current board state
void displayBoard()
{
	eraseDisplay();
	writeDebugStreamLine("\nBoard:");
	for(int row = Y_LENGTH-1; row >= 0; row--){
		for(int col = 0; col < X_LENGTH; col++)
		{
			displayStringAt(15+25*col, 25+20*row, "%c", getColourChar(board[row][X_LENGTH-col-1]));
			writeDebugStream("%c ", getColourChar(board[row][X_LENGTH-col-1]));
		}
		writeDebugStream("\n");
	}
	writeDebugStream("\n\n");
}

//outputs old board state
void displayOldBoard()
{
	eraseDisplay();
	writeDebugStreamLine("\nOld Board:");
	for(int row = Y_LENGTH-1; row >= 0; row--){
		for(int col = 0; col < X_LENGTH; col++)
		{
			displayStringAt(15+25*col, 25+20*row, "%c", getColourChar(old_board[row][X_LENGTH-col-1]));
			writeDebugStream("%c ", getColourChar(old_board[row][X_LENGTH-col-1]));
		}
		writeDebugStream("\n");
	}
	writeDebugStream("\n\n");
}

bool personThere()
{
	return SensorValue[US_PORT] < 75;
}

//checks if there is a location in which the robot can go to win or block the player from winning
int potentialWin(TLegoColors colour)
{
	int num_in_row = 0;
	int blank_row = 0;
	int blank_col = -1;
	int blank_num = 0;
	//horizontal check
	for (int row = 0; row<Y_LENGTH; row++)
	{
		num_in_row = 0;
		blank_num=0;
		blank_col=-1;
		blank_row=0;

		for (int col = 0; col<X_LENGTH; col++)
		{
			if (board[row][col]==colour || board[row][col]==colorNone)
			{
				if (board[row][col]==colorNone)
				{
					blank_num++;
					if (blank_num==2)
					{
						col = blank_col;
						row = blank_row;
						num_in_row = 0;
						blank_num=0;
					}
					else
					{
						blank_col = col;
						blank_row = row;
						num_in_row++;
					}
				}
				else
				{
					num_in_row++;
				}
			}
			else
			{
				num_in_row=0;
				blank_num=0;
				blank_col=-1;
				blank_row=0;
			}
			if(num_in_row==4 && (blank_row == 0 || board[blank_row-1][blank_col] != colorNone))
			{
				return blank_col;
			}
		}
	}

	int check_row = 0;
	int check_col = 0;
	//positive slope
	for (int row = 0; row<3; row++)
	{
		for (int col = 3; col<X_LENGTH; col++)
		{
			num_in_row = 0;
			blank_num = 0;
			blank_col = -1;
			blank_row = 0;
			check_row = row;
			check_col = col;
			while(num_in_row<4 && (board[check_row][check_col]==colour || board[check_row][check_col]==colorNone) && blank_num<2 && check_row<Y_LENGTH && check_col>=0)
			{
				if (board[check_row][check_col]==colorNone)
				{
					blank_num++;
					blank_col = check_col;
					blank_row = check_row;
				}
				num_in_row++;
				check_col--;
				check_row++;
			}
			if (num_in_row==4 && (blank_row==0 || board[blank_row-1][blank_col] != colorNone) && blank_num<2)
			{
				return blank_col;
			}
		}
	}

	//negative slope
	for (int row = 0; row<3; row++)
	{
		for (int col = 0; col<4; col++)
		{
			num_in_row = 0;
			blank_num = 0;
			blank_col = -1;
			blank_row = 0;
			check_row = row;
			check_col = col;
			while(num_in_row<4 && (board[check_row][check_col]==colour || board[check_row][check_col]==colorNone) && blank_num<2 && check_row<Y_LENGTH && check_col<X_LENGTH)
			{
				if (board[check_row][check_col]==colorNone)
				{
					blank_num++;
					blank_col = check_col;
					blank_row = check_row;
				}
				num_in_row++;
				check_col++;
				check_row++;
			}
			if (num_in_row==4 && (blank_row==0 || board[blank_row-1][blank_col]!=colorNone) && blank_num<2)
			{
				return blank_col;
			}
		}
	}

	return -1;
}

//checks if there is 4 in a row of a given colour
bool winner(TLegoColors colour)
{
	//Checks for horizontal 4 in a row win
	int pieces_in_row = 0;
	for (int rows=0; rows<Y_LENGTH; rows++)
	{
		pieces_in_row = 0;
		for (int col=0; col<X_LENGTH; col++)
		{
			if (board[rows][col] == colour)
			{
				pieces_in_row++;
				if(pieces_in_row == 4)
				{
					return true;
				}
			}
			else
			{
				pieces_in_row = 0;
			}
		}
	}
	//checks for vertical 4 in a row
	pieces_in_row = 0;
	for (int col=0; col<X_LENGTH; col++)
	{
		pieces_in_row = 0;
		for (int rows=0; rows<Y_LENGTH; rows++)
		{
			if (board[rows][col] == colour)
			{
				pieces_in_row++;
				if(pieces_in_row == 4)
				{
					return true;
				}
			}
			else
			{
				pieces_in_row = 0;
			}
		}
	}
	//check diagonal with positive slope
	pieces_in_row = 0;
	for (int rows = 0; rows < 3; rows++)
	{
		for (int col = 3; col < X_LENGTH; col++)
		{
			int check_row = rows, check_col = col;
			pieces_in_row = 0;

			while (check_row<Y_LENGTH && check_col>=0 && board[check_row][check_col] == colour && pieces_in_row<4)
			{
				pieces_in_row++;
				check_row++;
				check_col--;
			}
			if (pieces_in_row==4)
			{
				return true;
			}
		}
	}
	//check diagonal with negative slope
	for (int rows = 0; rows < 3; rows++)
	{
		for (int col = 0; col < 4; col++)
		{
			int check_row = rows, check_col = col;
			pieces_in_row = 0;

			while (check_row<Y_LENGTH && check_col<X_LENGTH && board[check_row][check_col] == colour && pieces_in_row<4)
			{
				pieces_in_row++;
				check_row++;
				check_col++;
			}
			if (pieces_in_row==4)
			{
				return true;
			}
		}
	}

	return false;
}

//runs while waiting for the player to go
void playerMove(){
	display("Play, then press ENTER", false);
	waitForPress();
	playSound(soundBeepBeep);
}

//determines the ideal location for the robot to play
int robotStrategy()
{
	//Check where the player played piece (save column and row)
	int player_col = 0;
	int player_row = 0;
	bool loc_found = false;
	for(int row = 0; row < Y_LENGTH; row++)
	{
		for(int col = 0; col < X_LENGTH; col++)
		{
			if(!loc_found && board[row][col] != old_board[row][col])
			{
				player_col = col;
				player_row = row;
				loc_found = true;
				old_board[row][col] = PLAYER_COLOUR; //Updates old_board with the players move
			}
		}
	}

	int x_coord = -1;

	//Winning move
	x_coord = potentialWin(ROBOT_COLOUR);
	if (x_coord != -1) return x_coord;

	//Block the player from winning
	x_coord = potentialWin(PLAYER_COLOUR);
	if (x_coord != -1) return x_coord;

	//Play middle for empty board
	bool empty = true;
	for(int col = 0; col < X_LENGTH; col++)
	{
		if(empty && board[0][col] != colorNone) empty = false;
	}
	if(empty) return 3;

	if(player_row != Y_LENGTH-1) return player_col; //Check if column is valid to play in (check if column is full)

	//Find a new place to play by randomizing columns until an available spot is found
	writeDebugStreamLine("Randomizing");
	do
	{
		x_coord=random(X_LENGTH-1);
	} while (board[Y_LENGTH-1][x_coord]!=colorNone);
	return x_coord;

	return -1; //Should never happen
}

//finds the row to play in , updates array, and plays piece
void robotMove()
{
	display("Robot Moving...");
	int x_coord = robotStrategy();
	int y_coord = 0;
	if (x_coord < 0 || x_coord >= X_LENGTH) y_coord = -1;
	else
	{
		//Finds row from the column
		while(y_coord < Y_LENGTH && board[y_coord][x_coord] != 0) y_coord++;
	}

	//Saves move to board
	board[y_coord][x_coord] = ROBOT_COLOUR;
	old_board[y_coord][x_coord] = ROBOT_COLOUR;
	writeDebugStreamLine("Robot playing at (%d,%d)", y_coord, x_coord);

	dropPiece(x_coord);

	writeDebugStreamLine("After playing piece");
	display("Robot Moved");
}

//checks if the user cheated and outputs information
bool cheated(int changed, int row, int col)
{
	bool cheat = false;
	if(changed > 1)
	{
		writeDebugStreamLine("changed: %d | row:%d, col:%d", changed, row, col);
		writeDebugStreamLine("old_board[%d][%d] == %c", row, col, getColourChar(old_board[row][col]));
		writeDebugStreamLine("board[%d][%d] == %c", row, col, getColourChar(board[row][col]));
		cheat = true;
	}
	if(old_board[row][col] != colorNone)
	{
		writeDebugStreamLine("old_board[%d][%d] != colorNone", row, col);
		writeDebugStreamLine("old_board[%d][%d] == %c", row, col, getColourChar(old_board[row][col]));
		writeDebugStreamLine("board[%d][%d] == %c", row, col, getColourChar(board[row][col]));
		cheat = true;
	}
	if(board[row][col] == ROBOT_COLOUR)
	{
		writeDebugStreamLine("old_board[%d][%d] == %c", row, col, getColourChar(old_board[row][col]));
		writeDebugStreamLine("board[%d][%d] == ROBOT_COLOUR", row, col);
		cheat = true;
	}

	if(cheat)
	{
		displayBoard();
		displayOldBoard();
		motor[SLIDE_PORT] = 0;
	}

	return cheat;
}

//scans through entire board
bool updateBoard()
{
	display("Scanning Board...");
	resetMotors();
	int changed = 0;
	for(int row = 0; row < 5; row++){
		moveY(DELTA_Y*row);
		motor[LIFT_PORT] = 0;
		wait1Msec(150); //Can we reduce this
		bool row_empty = true;

		for(int col = 0; col < X_LENGTH; col++){
			int column = (row % 2) == 0 ? col : X_LENGTH-col-1;
			moveX(DELTA_X*column);
			board[row][column] = getColour();
			writeDebugStreamLine("%c", getColourChar(board[row][column]));

			if(board[row][column] != old_board[row][column])
			{
				changed++;
				if(cheated(changed, row, column)) return true;
			}
			if(board[row][column] != colorNone) row_empty = false;
		}
		motor[SLIDE_PORT] = 0;

		if(row_empty)
		{
			writeDebugStreamLine("Early exit due to row %d being empty", row);
			if(changed != 1)
			{
				writeDebugStreamLine("changed: %d", changed);
				displayBoard();
				displayOldBoard();
				return true;
			}
			engageMag();
			return false;
		}
	}

	engageMag();

	//6th row alone outside loop
	const int row = 5;
	for(int col = 0; col < X_LENGTH; col++){

		moveX(DELTA_X*col, 20);
		motor[SLIDE_PORT] = 0;
		wait1Msec(300);
		if(col == X_LENGTH - 1) wait1Msec(200);

		board[row][col] = getColour();
		writeDebugStreamLine("%c", getColourChar(board[row][col]));

		if(board[row][col] != old_board[row][col])
		{
			changed++;
			if(cheated(changed, row, col))
			{
				moveX(MAG_RETURN);
				motor[SLIDE_PORT] = 0;
				return true;
			}
		}
	}

	writeDebugStreamLine("After scanning");
	display("Board Scan Complete");

	if(changed != 1)
	{
		writeDebugStreamLine("changed: %d", changed);
		moveX(MAG_RETURN);
		motor[SLIDE_PORT] = 0;
		displayBoard();
		displayOldBoard();
		return true;
	}
	return false;
}

//waits for the user to decide if they want to play again
bool playAgain()
{
	display("Play again?");
	displayCenteredTextLine(3, "Your Score is %d, score");
	setLEDColor(ledOrangePulse);
	displayStringAt(40, 58, "N");
	drawLine(50, 40, 50, 70);
	drawLine(30, 55, 50, 70);
	drawLine(50, 40, 30, 55);
	displayStringAt(135, 58, "Y");
	drawLine(130, 40, 130, 70);
	drawLine(150, 55, 130, 70);
	drawLine(130, 40, 150, 55);
	return waitForPress(buttonLeft, buttonRight) == buttonRight;
}

//shuts down by resetting board and saving score
void shutDown()
{
	stopAllMotors();
	display("\nShutting Down...");
	playSoundFile("Goodbye.rsf");
	setLEDColor(ledRedPulse);
	if(-nMotorEncoder[LIFT_PORT] > 680){
		moveX(MAG_RETURN);
		nMotorEncoder[SLIDE_PORT] = 0;
	}
	saveScore(getScore());
	resetBoard();
	stopAllTasks();
}

//reads and returns high score from file
short getScore()
{
	short high_score = 0;
	writeDebugStreamLine("Opening File to Read");
	long FileIn = fileOpenRead("Wins");
	if(FileIn == -1)
	{
		fileClose(FileIn);
		display("File not found!");
		writeDebugStreamLine("Closing File");
		setLEDColor(ledRedPulse);
		playSound(soundException);
		saveScore(0);
	}
	else
	{
		fileReadShort(FileIn, &high_score);
		fileClose(FileIn);
		writeDebugStreamLine("High Score is %d", high_score);
		writeDebugStreamLine("Closing File");
	}
	return high_score;
}

//saves score to file if higher than current high score
void saveScore(short high_score)
{
	if (score > high_score)
	{
		high_score = score;
	}
	writeDebugStreamLine("Opening File to Write");
	long FileOut = fileOpenWrite("Wins");
	fileWriteLong(FileOut, high_score);
	fileClose(FileOut);
	writeDebugStreamLine("Closing File");
}