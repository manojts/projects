import java.awt.*;
import java.applet.*;
import java.awt.event.*;
/*<applet code="Traffic" width=700 height=600>
</applet>*/
public class Traffic extends Applet implements Runnable
{
	Thread t;
	int i=0,a=0,j=0;
	public void start()
	{
		t=new Thread(this);
		t.start();
	}
	public void run()
	{
		for(i=20;i>=0;i--)//countdown
		{
			try
			{
				Thread.sleep(1000);
			}
			catch(Exception e)
			{
				System.out.println(e);
			}
			if(i<=20 && i>3)//red
			{
				a=1;
				repaint();
			}
			else
			if(i<=3 && i>0)//yelloe
			{
				a=2;
				repaint();
			}
			else
			if(i==0)//green
			{
				for(j=0;j<20;j++)
				{
					a=3;
					try
					{
						Thread.sleep(1000);
					}
					catch(Exception e)
					{
						System.out.println(e);
					}
					repaint();
				}
				if(j==20)//end of green(return to red)
				{
					run();
				}
			}
		}
		repaint();
	}
	public void paint(Graphics g)
	{
		g.setColor(Color.blue);
		g.drawString("Line-1",200,100);
		g.drawString("Walk line-1",200,600);

		g.setColor(Color.black);//pole top
		g.fillRect(200,150,50,150);
		g.drawRect(200,150,50,150);
		g.setColor(Color.black);//POLE UP
		g.fillRect(200,150,50,150);
		g.drawRect(200,150,50,150);
		g.setColor(Color.black);//POLE DOWN
		g.fillRect(215,300,20,155);
		g.drawRect(215,300,20,155);
		g.drawOval(200,150,50,50);//RED
		g.drawOval(200,200,50,50);//YELLOW
		g.drawOval(200,250,50,50);//GREEN
		//COUNTDOWN STOP
		


		g.setColor(Color.black);//pole top
		g.fillRect(200,500,50,50);
		g.drawRect(200,500,50,50);
		g.drawOval(200,150,50,50);

		g.setColor(Color.blue);
		g.drawString("Line-2",650,100);
		g.drawString("Walk line-2",650,600);

		g.setColor(Color.black);//pole top
		g.fillRect(650,150,50,150);
		g.drawRect(650,150,50,150);
		g.setColor(Color.black);//POLE UP
		g.fillRect(650,150,50,150);
		g.drawRect(650,150,50,150);
		g.setColor(Color.black);//POLE DOWN
		g.fillRect(665,300,20,155);
		g.drawRect(665,300,20,155);
		g.drawOval(650,150,50,50);//RED
		g.drawOval(650,200,50,50);//YELLOW
		g.drawOval(650,250,50,50);//GREEN
		
		g.setColor(Color.red);//COUNTDOWN STOP
		g.drawString(""+i,200,50);

		g.setColor(Color.black);//pole top
		g.fillRect(650,500,50,50);
		g.drawRect(650,500,50,50);
		g.drawOval(650,150,50,50);


		if(a==1)//REDSIGNAL
		{
			g.setColor(Color.red);//line-1
			g.fillOval(200,150,50,50);
			g.drawOval(200,150,50,50);
			g.drawString("STOP",50,150);

			g.fillOval(650,500,50,50);//walkline-2
			g.drawOval(650,500,50,50);

			g.setColor(Color.green);//line-2
			g.fillOval(650,250,50,50);
			g.drawOval(650,250,50,50);
			g.drawString("GO",550,150);

			g.fillOval(200,500,50,50);//walkline-1
			g.drawOval(200,500,50,50);
		}
		if(a==2)//YELLOWSIGNAL
		{
			g.setColor(Color.yellow);//line-1
			g.fillOval(200,200,50,50);
			g.drawOval(200,200,50,50);
			g.drawString("READY",50,200);

			g.setColor(Color.yellow);//line-2
			g.fillOval(650,200,50,50);
			g.drawOval(650,200,50,50);
			g.drawString("READY",550,200);
		}
		if(a==3)//GREENSIGNAL
		{
			g.setColor(Color.blue);//countdown
			g.drawString(""+j,650,50);
			g.setColor(Color.green);//line-1
			g.fillOval(200,250,50,50);
			g.drawOval(200,250,50,50);
			g.drawString("GO",50,250);

			g.fillOval(650,500,50,50);//walkline-2
			g.drawOval(650,500,50,50);

			
			g.setColor(Color.red);//line-2
			g.fillOval(650,150,50,50);
			g.drawOval(650,150,50,50);
			g.drawString("STOP",550,250);

			g.fillOval(200,500,50,50);//walkline-1
			g.drawOval(200,500,50,50);

			
		}
	}
}
