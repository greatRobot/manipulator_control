#include "sys.h"
#include "delay.h"
#include "usart.h"
#include "led.h"
#include "pwm.h"

int main(void)
{ 
 
	u8 len,t;	    //�������ݵĸ���
	u16 times=0;  
	u16 val[2];   //tim3����·ͨ���ļ���ֵ
	u16 servo0pwmval=0; //��һ·pwm�ź�ռ�ձȣ����0�����ؽ�0��ת����Ϣ��
  u16 servo1pwmval=0; //�ڶ�·pwm�ź�ռ�ձȣ����1�����ؽ�1��ת����Ϣ��
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);//����ϵͳ�ж����ȼ�����2��2�ж���ռ��2.��������
	delay_init(168);		//��ʱ��ʼ�� 
	TIM3_PWM_Init(200-1,8400-1);	//84M/8400=0.01Mhz�ļ���Ƶ��,��װ��ֵ500������PWMƵ��Ϊ 0.01M/200=50hz. ������ڴ�ԼΪ20ms
	uart_init(115200);	//���ڳ�ʼ��������Ϊ115200
	LED_Init();		  		//��ʼ����LED���ӵ�Ӳ���ӿ�  
	while(1)
	{   //USART_RX_STA������״̬�Ĵ���
		if(USART_RX_STA&0x8000)  //�Ƿ����������ɣ�1000��0000�� 0000�� 0000��
		{					   
			len=USART_RX_STA&0x3fff;//�õ��˴ν��յ������ݳ��ȣ�0011�� 1111�� 1111�� 1111��
			if(len==2)   //ֻ�е��Է��͵���2������ʱ����ִ�в���
			{
				servo0pwmval = USART_RX_BUF[0];
				servo1pwmval = USART_RX_BUF[1];
				USART_SendData(USART1, servo0pwmval);//������Ҫ��16���������ͣ�175-195����AFH- C3H��
				TIM_SetCompare1(TIM3,servo0pwmval);	//�޸ıȽ�ֵ���޸�ռ�ձ�
				TIM_SetCompare2(TIM3,servo1pwmval);	//�޸ıȽ�ֵ���޸�ռ�ձ�
				printf("\r\n����������\r\n");
			}
			else if(len==1){//�����͵�ǰ����ĽǶ�,����ѯTIM�ļ�����ֵ
				printf("\r\n��ǰ�ؽڽǣ�\r\n");
				val[0] = TIM3->CCR1;
				val[1] = TIM3->CCR2;
				for(t=0;t<2;t++){
						USART_SendData(USART1, val[t]);         //�򴮿�1��������
						while(USART_GetFlagStatus(USART1,USART_FLAG_TC)!=SET);//�ȴ����ͽ���
				}
			}
			else {
					printf("\r\n����������󣨼�ֻ������2���ؽڽ����ݣ�������������!\r\n");
			}
			USART_RX_STA=0;   //���������ݣ�������ݽ������־��Ϊ�´ν���������׼����
		}
		else{						//������δ��������������ݽ���ʱ
			times++;
			if(times%500==0)printf("������ؽڽ�����,�Իس�������\r\n");  
			if(times%30==0)LED0=!LED0;//��˸LED,��ʾϵͳ��������.
			delay_ms(10);   
		}
	}
}

